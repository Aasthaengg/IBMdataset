def BellmanFord(s,N,Edge):
    INF=float("inf")
    dist=[INF]*N
    neg=[False]*N
    dist[s]=0
    for i in range(N-1):
        for f,t,c in Edge:
            if dist[t]>dist[f]+c and dist[f]!=INF:
                dist[t]=min(dist[t],dist[f]+c)
    for i in range(N):
        for f,t,c in Edge:
            if dist[t]>dist[f]+c and dist[f]!=INF:
                dist[t]=dist[f]+c
                neg[t]=True
            if neg[f]:
                neg[t]=True
    return dist,neg

n,m=map(int,input().split())
es=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    es.append((a-1,b-1,-c))
    
res, neg =BellmanFord(0,n,es)
if not neg[-1]:
    print(-res[-1])
else:
    print("inf")