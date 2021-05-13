n,m=map(int,input().split())
edge=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    edge[a].append((b,-c))

renew=[0]*(n+1)
INF=float('inf')
def bellmanford(s,n):
    d = [INF for i in range(n+1)]
    d[s]=0
    q=[s]
    while q:
        x=q.pop()
        dist=d[x]
        for v,cost in edge[x]:
                if d[v]>dist+cost:
                    d[v]=dist+cost
                    q.append(v)
                    renew[v]+=1
                    if renew[v]>n:
                        d[v]=-INF
    return d
d=bellmanford(1,n)
print(-d[n])