n,m=map(int,input().split())
a=[0]*(n+1)
b=[0]*(n+1)
for i in range(m):
  x,y=map(int,input().split())
  if x==1:
    a[y]=1
  if y==n:
    b[x]=1
ans=0
for i in range(n+1):
  ans+=a[i]*b[i]
if ans==0:
  print('IMPOSSIBLE')
else:
  print('POSSIBLE')