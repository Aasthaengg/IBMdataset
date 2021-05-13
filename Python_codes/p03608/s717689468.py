from itertools import*
n,m,r=map(int,input().split())
rc=list(map(int,input().split()))
INF=10**18
d=[[INF]*n for _ in range(n)]
for _ in range(m):
  a,b,c=map(int,input().split())
  d[a-1][b-1]=c
  d[b-1][a-1]=c
for k in range(n):
  for i in range(n):
    for j in range(n):
      d[i][j]=min(d[i][j],d[i][k]+d[k][j])
ans=INF
for i in permutations(rc):
  a=0
  i=list(i)
  for j in range(r-1):
    a+=d[i[j]-1][i[j+1]-1]
  ans=min(a,ans)
print(ans)