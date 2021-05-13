import copy
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
b=copy.deepcopy(a)
for k in range(n):
  for i in range(n):
    for j in range(n):
      b[i][j]=min(b[i][j],b[i][k]+b[k][j])
for i in range(n):
  for j in range(n):
    if b[i][j]!=a[i][j]:
      print(-1)
      exit()
ans=0
for i in range(n):
  for j in range(i+1,n):
    m=10**18
    for k in range(n):
      if i==j or j==k or k==i:
        continue
      m=min(m,b[i][k]+b[k][j])
    if m>b[i][j]:
      ans+=b[i][j]
print(ans)