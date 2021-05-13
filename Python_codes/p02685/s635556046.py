N, M, K = map(int, input().split())
MOD = 998244353

ans = 0

class combination():
    def __init__(self, n):
        self.fact = [1] * (n+1)
        self.ifact = [1] * (n+1)
        for i in range(1, n+1):
            self.fact[i] = self.fact[i-1]*i % MOD
        self.ifact[n] = pow(self.fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            self.ifact[i-1] = self.ifact[i]*i % MOD
    def comb(self, n, k):
        if k < 0 or k > n: return 0
        comb = self.fact[n]*self.ifact[k]*self.ifact[n-k] %MOD
        return comb
comb = combination(N)

  
for k in range(K+1):
  # M x (N-1)Ck x (M-1) ^ (N - 1 - k)
  ans += (comb.comb(N-1, k) * pow(M-1, N-1-k, MOD)) % MOD
  
print(ans * M % MOD)