class BIT:
    def __init__(self, n, MOD):
        self.n = n
        self.data = [0] * (n + 1)
        self.MOD = MOD

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            s %= self.MOD
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            self.data[i] %= self.MOD
            i += i & -i


n, k = map(int, input().split())
mod = 998244353
bit = BIT(n + 2, mod)
ranges = []
for _ in range(k):
    l, r = map(int, input().split())
    ranges.append((l, r))

bit.add(1, 1)

for i in range(1, n):
    v = bit.sum(i)
    for l, r in ranges:
        bit.add(i + l, v)
        bit.add(min(n + 1, i + r + 1), -v)
print((bit.sum(n) - bit.sum(n - 1)) % mod)
