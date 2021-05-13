import heapq

n,m=map(int,input().split())
g=[[] for _ in range(n)]

for _ in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    g[a].append((b,c))
    g[b].append((a,c))

used=set()

for i in range(n):
    q=[(0,i,-1)]
    dist=[10**10]*n
    dist[i]=0
    edge=[0]*n

    while len(q)>0:
        d,u,v=heapq.heappop(q)

        if d>dist[u]:
            continue

        edge[u]=v

        for w,nd in g[u]:
            tmp=nd+dist[u]
            if tmp<dist[w]:
                dist[w]=tmp
                heapq.heappush(q,(tmp,w,u))
    
    for u,v in enumerate(edge):
        if v==-1:
            continue
        used.add((max(u,v),min(u,v)))

print(m-len(used))
