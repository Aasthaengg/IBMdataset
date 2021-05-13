import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

sys.setrecursionlimit(10**7)

ni = lambda: int(ns())
nin = lambda y: [ni() for _ in range(y)]
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda y: [na() for _ in range(y)]
nf = lambda: float(ns())
nfn = lambda y: [nf() for _ in range(y)]
nfa = lambda: list(map(float, stdin.readline().split()))
nfan = lambda y: [nfa() for _ in range(y)]
ns = lambda: stdin.readline().rstrip()
nsn = lambda y: [ns() for _ in range(y)]
ncl = lambda y: [list(ns()) for _ in range(y)]
nas = lambda: stdin.readline().split()

class Combination:
    def __init__(self, max_n=100007, mod=mod):
        self.mod = mod
        self.fac = [0] * max_n
        self.finv = [0] * max_n
        self.inv = [0] * max_n

        self.fac[0] = 1
        self.fac[1] = 1
        self.finv[0] = 1
        self.finv[1] = 1
        self.inv[1] = 1
        for i in range(2, max_n):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv[i] = self.mod - self.inv[self.mod % i] * (self.mod //
                                                               i) % self.mod
            self.finv[i] = self.finv[i - 1] * self.inv[i] % self.mod

    def choose(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.fac[n] * (self.finv[k] * self.finv[n - k] %
                              self.mod) % self.mod

n, k = na()
com = Combination(2007)

prev = 0
for i in range(1, k + 1):
    res = com.choose(n - k + 1, i)
    res *= com.choose(k - 1, i - 1)
    res %= mod
    print(res)

