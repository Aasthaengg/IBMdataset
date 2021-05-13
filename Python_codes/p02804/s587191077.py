import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

n,k = map(int,input().split())
a = list(map(int,input().split()))

mod = 10**9 + 7
fac = [1]*(n+5)
inv = [1]*(n+5)
for i in range(1,n+1):
  fac[i] = (fac[i-1]*i) % mod  
inv[n] = pow(fac[n], mod-2, mod)
for i in range(n, 0, -1):
  inv[i-1] = (inv[i]*i) % mod
    
def cmb(n, r):
  if r < 0 or r > n: return 0

  return (((fac[n] * inv[r])%mod) * inv[n-r]) % mod

ans=0
a.sort()
for h in range(2):
  for i in range(n):
    now = cmb(i,k-1)%mod
    if h == 1:now = -now
    ans += now*a[i]%mod

  a.sort(reverse=True)

print(ans%mod)
