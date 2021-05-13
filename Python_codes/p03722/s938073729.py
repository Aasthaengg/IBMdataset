n,m=map(int,input().split())
e=[list(map(int, input().split()))for _ in range(m)]
inf=float("inf")
d=[inf]*(n+1)
d[1]=0
for _ in range(n):
    for a,b,c in e:d[b]=min(d[b],d[a]-c)
x=d[n]
for a,b,c in e:d[b]=min(d[b],d[a]-c)
if x!=d[n]:print(inf)
else:print(-x)