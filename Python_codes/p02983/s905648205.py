l,r=map(int,input().split())
mod=2019
a=l%mod
b=l//mod
c=r%mod
d=r//mod
if d-b!=0:
  print(0)
else:
  ans=float('inf')
  for i in range(l,r):
    for j in range(i+1,r+1):
      ans=min(ans,(i*j)%mod)
  print(ans)