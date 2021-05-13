class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

n, m = map(int, input().split())
p = list(map(lambda x:int(x)-1, input().split()))

i2p = {}
p2i = {}

for i, pi in enumerate(p):
    i2p[i] = pi
    p2i[pi] = i

xy = [list(map(lambda x:int(x)-1, input().split())) for _ in range(m)]

uf = UnionFind(n)

for x, y in xy:
    uf.union(i2p[x], i2p[y])

ans = 0
for pi in p:
    if uf.find(pi) == uf.find(i2p[pi]):
        ans += 1

print(ans)