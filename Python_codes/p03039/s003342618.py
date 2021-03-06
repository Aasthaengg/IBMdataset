class ModCalc:
    mod = 10**9 + 7

    def __init__(self, n):
        self.n = n
        self.inv = [1] * (self.n + 1)
        self.fac = [1] * (self.n + 1)
        self.finv = [1] * (self.n + 1)
        self.inv[0] = 0
        self.inv_table()

    def inv_table(self):
        for i in range(2, self.n+1):
            self.inv[i] = self.inv[self.mod % i] * (self.mod - self.mod // i) % self.mod
            self.fac[i] = self.fac[i-1] * i % self.mod
            self.finv[i] = self.finv[i-1] * self.inv[i] % self.mod

    def comb(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0

        return self.fac[n] * self.finv[r] % self.mod * self.finv[n-r] % self.mod

    def perm(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0

        return self.fac[n] * self.finv[n-r] % self.mod

    def fact(self, n):
        return self.fac[n]


n, m, k = map(int, input().split())

mc = ModCalc(n*m)
mod = 10**9 + 7

ret = 0
for d in range(1, n):
    ret += d * (n - d) % mod * m % mod * m % mod * mc.comb(n * m - 2, k-2) % mod
    ret %= mod

for d in range(1, m):
    ret += d * (m - d) % mod * n % mod * n % mod * mc.comb(n * m - 2, k - 2) % mod
    ret %= mod
print(ret)
