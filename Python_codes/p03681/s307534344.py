n,m=map(int,input().split())
mod=10**9+7
def kaijou(x):
  y=1
  for i in range(1,x+1):
    y*=i
    y%=mod
  return y
if abs(n-m)>=2:
  print(0)
elif n==m:
  print((kaijou(n)*kaijou(m)*2)%mod)
else:
  print((kaijou(n)*kaijou(m))%mod)
