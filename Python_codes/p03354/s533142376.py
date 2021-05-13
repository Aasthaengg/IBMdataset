import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
        self.parent = [-1 for _ in range(n)]
        # 正==子: 根の頂点番号 / 負==根: 連結頂点数

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        else:
            if self.size(x) < self.size(y):
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        x = self.find(x)
        return -self.parent[x]

    def is_root(self, x):
        return self.parent[x] < 0


N,M = map(int,input().split())
p = list(map(int,input().split()))
uf = UnionFind(N)
for i in range(M):
    x,y = map(int,input().split())
    uf.unite(x-1,y-1)

ans = 0
for i in range(N):
    if p[i]-1 == i:
        ans += 1
    else:
        if uf.same(p[i]-1,i):
            ans += 1
print(ans)