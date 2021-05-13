n,k=map(int,input().split())
class mod_comb_k():
  def __init__(self, MAX_N = 10**6, mod = 10**9+7):
    self.fact = [1]
    self.fact_inv = [0] * (MAX_N + 4)
    for i in range(MAX_N + 3):self.fact.append(self.fact[-1] * (i + 1) % mod)
    self.fact_inv[-1] = pow(self.fact[-1], mod - 2, mod)
    for i in range(MAX_N + 2, -1, -1):
      self.fact_inv[i] = self.fact_inv[i + 1] * (i + 1) % mod
  def comb(self, n, k, mod = 10**9+7):
    return self.fact[n] * self.fact_inv[k] % mod * self.fact_inv[n - k] % mod
c=mod_comb_k(n)
mod=10**9+7
for i in range(k):
  div=c.comb(k-1,i)
  if n-k+1>=i+1:print(c.comb(n-k+1,i+1)*div%mod)
  else:print(0)