n,k,*x=map(int,open(0).read().split())
ans=float('inf')
if 0 in x:
  k-=1
  n-=1
  del x[x.index(0)]

if k==0:
  print(0)
else:
  for i in range(n-k+1):
    ans=min(ans,abs(x[i])+abs(x[i]-x[i+k-1]))
  for i in range(k-1,n):
    ans=min(ans,abs(x[i])+abs(x[i]-x[i-(k-1)]))
  print(ans)