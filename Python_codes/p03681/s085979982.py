n,m=map(int,input().split())
mod=10**9+7
nkai=1
mkai=1
for i in range(1,n+1):
  nkai*=(i%mod)
  nkai=(nkai%mod)
for i in range(1,m+1):
  mkai*=(i%mod)
  mkai=(mkai%mod)
if abs(n-m)>=2:
  print(0)
elif abs(n-m)==1:
  print((mkai*nkai)%mod)
elif abs(n-m)==0:
  print((mkai*nkai*2)%mod)