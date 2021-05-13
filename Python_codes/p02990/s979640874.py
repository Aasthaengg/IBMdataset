# https://atcoder.jp/contests/abc132/tasks/abc132_d

MOD = 10**9 + 7

class Facts:
    def __init__(self, mod=10**9+7, n_max=1):
        self.mod     = mod
        self.n_max   = n_max
        self.fact    = [1, 1]
        self.inv     = [0, 1]
        self.factinv = [1, 1]
        if 1 < n_max:
            self.setup_table(n_max)
 
    def cmb(self, n, r):
        if r < 0 or n < r:
            return 0
        if self.n_max < n:
            self.setup_table(n)
        return self.fact[n] * (self.factinv[r] * self.factinv[n-r] % self.mod) % self.mod
 
    def setup_table(self, t):
        for i in range(self.n_max+1,t+1):
            self.fact.append( self.fact[-1] * i % self.mod )
            self.inv.append( -self.inv[self.mod % i] * (self.mod // i) % self.mod )
            self.factinv.append( self.factinv[-1] * self.inv[-1] % self.mod )
        self.n_max = t


fact = Facts()
n, k = map(int, input().split())
for i in range(1, k + 1):
    ans = fact.cmb(n - k + 1, i) * fact.cmb(k - 1, i - 1)
    ans %= MOD
    print(ans)