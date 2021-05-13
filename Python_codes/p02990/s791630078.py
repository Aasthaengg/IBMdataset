N, K = map(int, input().split())
M = N - K
mod = 10**9 + 7

class Combination:
    def __init__(self, n):
        self.facts = [1 for i in range(n+1)]
        self.invs = [1 for i in range(n+1)]
        
        for i in range(1, n+1):
            self.facts[i] = self.facts[i-1] * i % mod
            self.invs[i] = pow(self.facts[i], mod-2, mod)

    def ncr(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        else:
            return self.facts[n] * self.invs[r] * self.invs[n-r] % mod

    def nhr(self, n, r): 
        return self.ncr(n+r-1, n-1)

comb = Combination(max(M+1, K-1))

for i in range(K):
    ans = comb.ncr(M+1, i+1) * comb.ncr(K-1, i)
    print(ans%mod)