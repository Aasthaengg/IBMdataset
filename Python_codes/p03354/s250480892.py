# UnionFind、0-index
#############################################################


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, v):  # vが属する集合の根を返す
        if self.parents[v] < 0:
            return v
        else:
            self.parents[v] = self.find(self.parents[v])
            return self.parents[v]

    def unite(self, u, v):  # 「uが属する集合」と「vが属する集合」を併合（根同士を結ぶ）
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        if self.parents[u] > self.parents[v]:  # u < v に統一する
            u, v = v, u
        self.parents[u] += self.parents[v]
        self.parents[v] = u

    def size(self, v):  # vが属する集合の要素数
        return -self.parents[self.find(v)]

    def same(self, u, v):  # uとvが同じ集合に属するか否か
        return self.find(u) == self.find(v)
#############################################################
# (x,y)をuniteする
# i = 1,2,...,Nについて、
# iとp[i-1]が同じ連結成分に含まれるならば、p_i = iとすることができる

N, M = map(int, input().split())
p = list(map(int, input().split()))

uf = UnionFind(N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    uf.unite(x, y)
ans = 0
for i in range(1, N + 1):
    if uf.same(p[i - 1], i):
        ans += 1
print(ans)
