import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[0]*m
b=[0]*m
c=[0]*m
for i in range(m):
  a[i],b[i],c[i]=map(int,input().split())
  a[i]-=1
  b[i]-=1
INF=10**18#float('inf')
dist=[ [INF]*n for _ in range(n)]
for i in range(n):
  dist[i][i]=0
for i in range(m):
  dist[a[i]][b[i]]=c[i]
  dist[b[i]][a[i]]=c[i]
#floyd warshall
for k in range(n):
  for i in range(n):
    for j in range(n):
      dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
ans=m
for i in range(m):
  shortest=False
  for j in range(n):
    if dist[j][a[i]]+c[i]==dist[j][b[i]]:
      shortest=True
      break
  if shortest:
    ans-=1
print(ans)



