def comb(n,k,mod):
  a = 1
  b = 1
  for i in range(k):
    a = a * (n-i) % mod
    b = b * (i+1) % mod
  return a * pow(b, mod-2, mod) % mod
n,k=map(int,input().split())
mod=10**9+7
for i in range(1,k+1):
  print((comb(n-k+1,i,mod)*comb(k-1,i-1,mod))%mod)
