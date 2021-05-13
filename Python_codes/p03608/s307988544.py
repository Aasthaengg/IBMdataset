from itertools import permutations
INF=10**18
n,m,r=map(int,input().split())
dist=[[INF for _ in range(n+1)]for _ in range(n+1)]
dp=[[-1 for _ in range(r+1)]for _ in  range((1<<r)+1)]
r_t=list(map(int,input().split()))
for i in range(n+1):
  dist[i][i]=0
for _ in range(m):
  a,b,c=map(int,input().split())
  dist[a][b]=c
  dist[b][a]=c
for k in range(n+1):
  for i in range(n+1):
    for j in range(n+1):
      dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
r_list=list(permutations(r_t))
fans=INF
for i in r_list:
  ans=0
  for j in range(r-1):
    ans+=dist[i[j+1]][i[j]]
  fans=min(fans,ans)
print(fans)