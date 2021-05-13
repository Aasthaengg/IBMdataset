class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * (n)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

n, m = [int(_n) for _n in input().split()]
p = [int(_p)-1 for _p in input().split()]
x = []
y = []
for i in range(0,m):
    X,Y = [int(_n) for _n in input().split()]
    x.append(X-1)
    y.append(Y-1)

uf = UnionFind(n)

for i in range(0,m):
    uf.union(x[i],y[i])

ans = 0
for i in range(0,n):
    if uf.find(i) == uf.find(p[i]):
        ans += 1

print(ans)