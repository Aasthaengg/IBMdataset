from heapq import heappush,heappop,heapify
INF=10**30

def dijkstra(G,s,n):
    que=[(0,s)]
    dist=[INF]*n
    last=[-1]*n
    dist[s]=0
    while que:
        mincost,u=heappop(que)
        if(mincost>dist[u]):
            continue
        for c,v in G[u]:
            if(dist[u]+c<dist[v]):
                dist[v]=dist[u]+c
                last[v]=u
                heappush(que,(dist[v],v))
    return dist,last

dic={}
N,M=map(int,input().split())
G=[[] for i in range(N)]
Edges=[]
for i in range(M):
    a,b,c=map(int,input().split())
    a-=1;b-=1
    G[a].append((c,b))
    G[b].append((c,a))
    Edges.append(tuple(sorted([a,b])))

for i in range(N):
    dist,last=dijkstra(G,i,N)
    for j in range(i):
        now=j
        while(now!=i):
            nex=last[now]
            dic[tuple(sorted([now,nex]))]=1
            now=nex
ans=len(Edges)
for u,v in Edges:
    if (u,v) in dic:
        ans-=1
print(ans)