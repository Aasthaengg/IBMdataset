mod = 1000000007

class combination():
    def __init__(self, n):
        self.fact = [1] * (n+1)
        self.ifact = [1] * (n+1)
        for i in range(1, n+1):
            self.fact[i] = self.fact[i-1]*i % mod
        self.ifact[n] = pow(self.fact[n], mod-2, mod)
        for i in range(n, 0, -1):
            self.ifact[i-1] = self.ifact[i]*i % mod
    def comb(self, n, k):
        if k < 0 or k > n: return 0
        comb = self.fact[n]*self.ifact[k]*self.ifact[n-k] %mod
        return comb

n, k = map(int, input().split())

comb = combination(n)
for i in range(1, k+1):
    print(comb.comb(n-k+1, i) * comb.comb(k-1, i-1) % mod)