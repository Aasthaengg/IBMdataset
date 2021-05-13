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
AB = [list(map(int, input().split())) for _ in range(M)]
uf = UnionFind(N)
AB.reverse()
ans = [N * (N - 1) // 2]
for A, B in AB:
    if uf.same(A - 1, B - 1):
        ans.append(ans[-1])
    else:
        ans.append(ans[-1] - uf.size(A - 1) * uf.size(B - 1))
    uf.unite(A - 1, B - 1)

for a in ans[:-1][::-1]:
    print(a)
