class UnionFind:
    def __init__(self, size):
        self.data = [-1] * size
    def find(self, x):
        if self.data[x] < 0:
            return x
        else:
            self.data[x] = self.find(self.data[x])
            return self.data[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.data[y] < self.data[x]:
                x, y = y, x
            self.data[x] += self.data[y]
            self.data[y] = x
        return (x != y)
    def same(self, x, y):
        return (self.find(x) == self.find(y))
 
N, M, *I = map(int, open(0).read().split())
P, XY = I[:N], I[N:]
 
uf = UnionFind(N + 1)
for x, y in zip(*[iter(XY)] * 2):
    uf.union(x, y)
 
ans = 0
for i, p in enumerate(P, 1):
    if uf.same(i, p):
        ans += 1
 
print(ans)