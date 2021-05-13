n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

mod=10**9+7

MAX_N=n+5
fac = [1,1] + [0]*MAX_N
finv = [1,1] + [0]*MAX_N
inv = [0,1] + [0]*MAX_N
for i in range(2,MAX_N):
  fac[i] = fac[i-1] * i % mod
  inv[i] = mod - inv[mod % i] * (mod // i) % mod
  finv[i] = finv[i-1] * inv[i] % mod

def nCk(n,k):
  if n<k:
    return 0
  if n<0 or k<0:
    return 0
  return fac[n] * (finv[k] * finv[n-k] % mod) % mod

max_x=0
for i in range(k-1,n):
  max_x+=a[i]*nCk(i,k-1)
  max_x%=mod

min_x=0
for i in range(n-k+1):
  min_x+=a[i]*nCk(n-i-1,k-1)
  min_x%=mod

print((max_x-min_x)%mod)