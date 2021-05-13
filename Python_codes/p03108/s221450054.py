class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        x = self.find(x)
        return self.size[x]


n, m = map(int, input().split())

bridges = []
for i in range(m):
    a, b = map(int, input().split())
    bridges.append((a-1, b-1))

uf = UnionFind(n)
ans = [n * (n-1) // 2]
for a, b in bridges[::-1]:
    a1 = uf.get_size(a)
    b1 = uf.get_size(b)
    uf.union(a, b)
    a2 = uf.get_size(a)
    b2 = uf.get_size(b)

    conv = (a1 * (a2 - a1) + b1 * (b2 - b1)) // 2
    ans.append(ans[-1]-conv)

print('\n'.join(map(str, ans[-2::-1])))
