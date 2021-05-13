class UnionFind():
    def __init__(self, n):
        self.n = n
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

n,m = map(int,input().split())
Permutation = list(map(int,input().split()))
Replace = [list(map(int,input().split())) for i in range(m)]

uf = UnionFind(n+1)
count = 0

for i in range(m):
    uf.union(Replace[i][0],Replace[i][1])

for i in range(1,n+1):
    if uf.same(Permutation[i-1],i):
        count += 1

print(count)