INF=10**18
n=10
h,w=map(int,input().split())
dist=[list(map(int,input().split())) for _ in range(n)]
a=[list(map(int,input().split())) for _ in range(h)]
for k in range(n):
  for i in range(n):
    for j in range(n):
      dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
ans=0
for i in range(h):
  for j in range(w):
    if a[i][j]==-1:continue
    ans+=dist[a[i][j]][1]
print(ans)