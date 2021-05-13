N, K = map(int, input().split())

mod = 10 ** 9 + 7
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]

def comb(n, r):
  if n < r:
    return 0
  else:
    return fac[n] * ( finv[r] * finv[n-r] % mod ) % mod
 
for i in range(2, N + 1):
  fac.append( ( fac[-1] * i ) % mod )
  inv.append( mod - ( inv[mod % i] * (mod // i) % mod ) )
  finv.append( finv[-1] * inv[-1]  % mod )

for i in range(1, K+1):
  print(comb(N-K+1, i) * comb(K-1, i-1) % mod)