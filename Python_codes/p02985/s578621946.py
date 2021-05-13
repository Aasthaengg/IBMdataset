# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, K, G):
    fu = FactorialUtils(K)
    p = [-1] * N
    p[0] = 0
    stk = [0]
    ans = Mint(K)
    while stk:
        v = stk.pop()
        t = 1 if v != 0 else 0
        ans *= fu.permutation(K - t - 1, len(G[v]) - t)
        for to in G[v]:
            if p[to] >= 0:
                continue
            p[to] = v
            stk.append(to)
    print(ans)

MOD = 10**9 + 7
class FactorialUtils:
    def __init__(self, n):
        self.fac = [1] * (n + 1)
        self.ifac = [1] * (n + 1)
        for i in range(2, n + 1): self.fac[i] = self.fac[i - 1] * i % MOD
        self.ifac[n] = pow(self.fac[n], MOD - 2, MOD)
        for i in range(n, 1, -1): self.ifac[i - 1] = self.ifac[i] * i % MOD

    def choose(self, n, r):
        if r < 0 or r > n: return 0
        return (self.fac[n] * self.ifac[n - r] % MOD) * self.ifac[r] % MOD

    def multichoose(self, u, k):
        return (self.fac[u + k - 1] * self.ifac[u - 1] % MOD) * self.ifac[k] % MOD

    def permutation(self, n, r):
        if r < 0 or r > n: return 0
        return self.fac[n] * self.ifac[n - r] % MOD

class Mint:
    def __init__(self, value=0):
        self.value = value % MOD
        if self.value < 0: self.value += MOD

    @staticmethod
    def get_value(x): return x.value if isinstance(x, Mint) else x

    def inverse(self):
        a, b = self.value, MOD
        u, v = 1, 0
        while b:
            t = a // b
            b, a = a - t * b, b
            v, u = u - t * v, v
        if u < 0: u += MOD
        return u

    def __repr__(self): return str(self.value)
    def __eq__(self, other): return self.value == other.value
    def __neg__(self): return Mint(-self.value)
    def __hash__(self): return hash(self.value)
    def __bool__(self): return self.value != 0

    def __iadd__(self, other):
        self.value = (self.value + Mint.get_value(other)) % MOD
        return self

    def __add__(self, other):
        new_obj = Mint(self.value)
        new_obj += other
        return new_obj
    __radd__ = __add__

    def __isub__(self, other):
        self.value = (self.value - Mint.get_value(other)) % MOD
        if self.value < 0: self.value += MOD
        return self

    def __sub__(self, other):
        new_obj = Mint(self.value)
        new_obj -= other
        return new_obj

    def __rsub__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj -= self
        return new_obj

    def __imul__(self, other):
        self.value = self.value * Mint.get_value(other) % MOD
        return self

    def __mul__(self, other):
        new_obj = Mint(self.value)
        new_obj *= other
        return new_obj
    __rmul__ = __mul__

    def __ifloordiv__(self, other):
        other = other if isinstance(other, Mint) else Mint(other)
        self *= other.inverse()
        return self

    def __floordiv__(self, other):
        new_obj = Mint(self.value)
        new_obj //= other
        return new_obj

    def __rfloordiv__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj //= self
        return new_obj

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        x, y = map(int, input().split())
        x, y = x - 1, y - 1
        G[x].append(y)
        G[y].append(x)
    main(N, K, G)
