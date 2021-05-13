from heapq import heappush,heappop,heapify
INF=10**30
def dijkstra(G,s,n):
    que=[(0,s)]
    dist=[INF]*n
    dist[s]=0
    while que:
        mincost,u=heappop(que)
        if(mincost>dist[u]):
            continue
        for v,c in G[u]:
            if(dist[u]+c<dist[v]):
                dist[v]=dist[u]+c
                heappush(que,(dist[v],v))
    return dist
N=int(input())
G=[[] for i in range(N)]
for i in range(N-1):
    a,b,c=map(int,input().split())
    G[a-1].append([b-1,c])
    G[b-1].append([a-1,c])
Q,K=map(int,input().split())
dist=dijkstra(G,K-1,N)
for i in range(Q):
    x,y=map(lambda x:int(x)-1,input().split())
    print(dist[x]+dist[y])