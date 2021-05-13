class UnionFind:
    """素集合を木構造として管理する"""
    def __init__(self, n):
        self.parent = [-1] * n
        self.cnt = n

    def root(self, x):
        """要素xの根を求める"""
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        """要素xを含む集合と要素yを含む集合を統合する"""
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.cnt -= 1

    def is_same(self, x, y):
        """要素x, yが同じ集合に属するかどうかを求める"""
        return self.root(x) == self.root(y)

    def get_size(self, x):
        """要素xを含む集合の要素数を求める"""
        return -self.parent[self.root(x)]


n, k, l = map(int, input().split())
info_k = [list(map(int, input().split())) for i in range(k)]
info_l = [list(map(int, input().split())) for i in range(l)]

ufk = UnionFind(n)
ufl = UnionFind(n)
uf_total = UnionFind(n)

for a, b in info_k:
    a -= 1
    b -= 1
    ufk.merge(a, b)

for a, b in info_l:
    a -= 1
    b -= 1
    ufl.merge(a, b)

pair_cnt = {}
for i in range(n):
    if (ufk.root(i), ufl.root(i)) not in pair_cnt:
        pair_cnt[ufk.root(i), ufl.root(i)] = 1
    else:
        pair_cnt[ufk.root(i), ufl.root(i)] += 1

ans = [pair_cnt[ufk.root(i), ufl.root(i)] for i in range(n)]
print(*ans)