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
            return 0
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        
N,M,*f = map(int, open(0).read().split())
AB = [f[i*2:i*2+2] for i in range(M)]
uf = UnionFind(N)
for A,B in AB:
    uf.union(A-1,B-1)
print(min(uf.parents)*(-1))