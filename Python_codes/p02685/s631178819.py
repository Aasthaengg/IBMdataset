n, m, k = map(int, input().split())
mod = 998244353

ans = 0
t = 1
b = 1
for i in range(k+1):
  ans += t * pow(m-1, n-1-i, mod) * pow(b, mod-2, mod)
  ans %= mod
  #n-1Ci * (m-1)**i
  t *= (n-1-i)
  t %= mod
  b *= (i+1)
  b %= mod
print(ans*m%mod)