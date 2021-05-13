n=int(input())
dis=[list(map(int,input().split())) for _ in range(n)]
c=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    c[i][j]=min(dis[i][k]+dis[k][j] for k in range(n))
for i in range(n):
  for j in range(n):
    if c[i][j]!=dis[i][j]:
      print(-1)
      exit()
for i in range(n):
  for j in range(n):
    for k in range(n):
      if i==k or j==k:continue
      if dis[i][j]==dis[i][k]+dis[k][j]:c[i][j]=0
print(sum(sum(c[i]) for i in range(n))//2)