import sys
sys.setrecursionlimit(1000000)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        # 親の番号 根なら要素数(負の数)

    def find(self, x):
        """木の根を求める"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        """xとyの属する集合を併合"""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        """xとyが同じ集合に属するか否か"""
        return self.find(x) == self.find(y)

    def size(self, x):
        """グループのサイズを返す"""
        return -self.parents[self.find(x)]

N , M = map(int, input().split())
p = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(M)]
uf = UnionFind(N)
for x, y in xy:
    uf.unite(x - 1, y - 1)
ans = 0

for i in range(N):
    if uf.same(i, p[i] - 1):
        ans += 1

print(ans)
