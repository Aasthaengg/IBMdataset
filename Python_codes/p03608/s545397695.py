import itertools
n,m,r=map(int,input().split())
point=list(map(int,input().split()))
g=[[10**9]*n for i in range(n)]
for _ in range(m):
  u,v,c=map(int,input().split())
  g[u-1][v-1]=g[v-1][u-1]=c
for k in range(n):
  for i in range(n):
    for j in range(n):
      g[i][j]=min(g[i][j],g[i][k]+g[k][j])
for i in range(n):
  g[i][i]=0
ans=10**18
for v in itertools.permutations(point):
  tmp=0
  for i in range(r-1):
    tmp+=g[v[i]-1][v[i+1]-1]
  ans=min(ans,tmp)
print(ans)