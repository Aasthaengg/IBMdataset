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
uf = UnionFind(n)

for i in range(m):
    a, b = map(int, input().split())
    uf.union(a-1,b-1)

cnt = 0
for item in uf.parents:
    if item < 0:
        cnt += 1

print(cnt-1)