class UnionFind:
    def __init__(self, n):
        self.par = [-1] * (n + 1)  # 頂点番号とindexをそろえるためにn+1
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])  # 再帰で根までたどる.その過程で根とつなぎかえる
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        else:
            if self.rank[x] < self.rank[y]:
                self.par[y] += self.par[x]
                self.par[x] = y
            else:
                self.par[x] += self.par[y]
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)  # 根同じならTrue違うならFalseを返す

    def size(self, x):
        return -self.par[self.find(x)]


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

uf = UnionFind(n)
res = n*(n-1)//2
ans = []
ans.append(res)
for i in range(1, m)[::-1]:
    a = ab[i][0]
    b = ab[i][1]
    if not uf.same_check(a, b):
        res -= uf.size(a)*uf.size(b)
    uf.union(a, b)
    ans.append(res)
ans.reverse()
for i in range(m):
    print(ans[i])

