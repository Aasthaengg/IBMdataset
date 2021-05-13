x,y = map(int,input().split())
mod = 10**9+7
if (x+y)%3!=0:
  print(0)
  exit()
if 2*min(x,y)<max(x,y):
  print(0)
  exit()
n = (2*x-y)//3
m = (2*y-x)//3
#n+mCm
if n==0 or m==0:
  print(1)
  exit()
def ka(x):
  a = 1
  while x!=1:
    a *= x
    x -= 1
    a%= mod
  return a

ans = (ka(n+m)*pow(ka(m),mod-2,mod)%mod)*(pow(ka(n),mod-2,mod))%mod
print(ans)