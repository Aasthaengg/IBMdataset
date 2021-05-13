def make_array_for_comb(N, mod=10**9+7):
    fact = [1,1]
    fact_inv = [1,1]
    inv = [0,1]
    for i in range(2, N+1):
        fact.append((fact[-1]*i) % mod)
        # モジュラ逆数の性質
        inv.append((-inv[mod%i] * (mod//i)) % mod)
        fact_inv.append((fact_inv[-1]*inv[i]) % mod)
    return fact, fact_inv

def comb(n, r, mod=10**9+7):
  if (r < 0) or (n < r):
      return 0
  r = min(r, n - r)
  return fact[n] * fact_inv[r] * fact_inv[n-r] % mod

n,k = [int(i) for i in input().split()]
mod = 10**9+7
fact, fact_inv = make_array_for_comb(n,mod)
ans = 0

for i in range(min(n,k+1)):
  ans += (comb(n,i,mod)*comb(n-1,i,mod)%mod)
  ans %= mod
  
print(ans)