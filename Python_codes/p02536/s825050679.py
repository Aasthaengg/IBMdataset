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
    def size(self, x):
        return -self.data[self.find(x)]

N, M, *AB = map(int, open(0).read().split())

uf = UnionFind(N)
for a, b in zip(*[iter(AB)] * 2):
    uf.union(a - 1, b - 1)

print(len({uf.find(i) for i in range(N)}) - 1)