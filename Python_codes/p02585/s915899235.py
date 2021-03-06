def solve():
    from collections import defaultdict
    class UnionFind():
        def __init__(self, n):
            self.n = n
            self.par = [-1] * n

        def find(self, x):
            if self.par[x] < 0:
                return x
            else:
                while self.par[x] >= 0:
                  x = self.par[x]
                return x

        def unite(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.par[x] > self.par[y]:
                x, y = y, x

            self.par[x] += self.par[y]
            self.par[y] = x

        def size(self, x):
            return -self.par[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    mp = defaultdict(int)
    uf = UnionFind(n)

    for i in range(n):
        uf.unite(i, p[i] - 1)

    for i in range(n):
        mp[uf.find(i)] += c[i]

    ans = -10 ** 14
    for i in range(n):
        roop = uf.size(i)
        times = (k - 1) // roop if mp[uf.find(i)] > 0 else 0
        over = max(min(roop, k - roop * times), 1)
        tmp = 0
        s = -10 ** 10
        idx = i
        for j in range(over):
            tmp += c[idx]
            s = max(s, tmp)
            idx = p[idx] - 1
        s += times * mp[uf.find(i)]
        ans = max(ans, s)
    print(ans)


solve()
