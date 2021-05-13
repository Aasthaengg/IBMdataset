class UnionFind():
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.size = [1 for _ in range(N)]

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
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            elif self.rank[x] < self.rank[y]:
                x, y = y, x
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_size(self, x):
        x = self.find(x)
        return self.size[x]

N, M = map(int, input().split())
P = list(map(int, input().split()))
uf = UnionFind(N)
for i in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    uf.union(x, y)

ans = 0
for i in range(N):
    if uf.is_same(i, P[i]-1):
        ans += 1

print(ans)