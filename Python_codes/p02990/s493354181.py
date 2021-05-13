def cmb(n, r, p):
  if (r < 0) or (n < r):
    return 0
  r = min(r, n - r)
  return fact[n] * factinv[r] * factinv[n-r] % P

N, K = map(int, input().split())
P = 10**9 + 7
r = N - K
fact = [1, 1]  
factinv = [1, 1] 
inv = [0, 1] 
 
for i in range(2, N + 1):
  fact.append((fact[-1] * i) % P)
  inv.append((-inv[P % i] * (P // i)) % P)
  factinv.append((factinv[-1] * inv[-1]) % P)

for i in range(1,K+1):
  print(cmb(r+1, i, P)*cmb(K-1, i-1, P) % P)