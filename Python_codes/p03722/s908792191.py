n,m=map(int,input().split())
edge=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    edge[a].append((b,-c))

renew=set()
from heapq import *
INF=float('inf')
def dijkstra(s,n):
    d = [INF for i in range(n+1)]
    pq = []
    d[s]=0
    heappush(pq,(0,s))
    while pq:
        dist,u = heappop(pq)
        for v,cost in edge[u]:
            if d[v]<=dist+cost:
                continue
            d[v]=dist+cost
            if (u,v) in renew:
                d[v]=-INF
            renew.add((u,v))
            heappush(pq,(d[v],v))
    return d             
d=dijkstra(1,n)
print(-d[n])