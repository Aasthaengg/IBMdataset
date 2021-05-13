n,m,q=map(int,input().split())
a=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
  l,r=map(int,input().split())
  a[l][r]+=1
for i in range(n+1):
  for j in range(n):
    a[i][j+1]+=a[i][j]
for i in range(n):
  for j in range(n+1):
    a[i+1][j]+=a[i][j]
for _ in range(q):
  q,p=map(int,input().split())
  print(a[p][p]-a[p][q-1]-a[q-1][p]+a[q-1][q-1])