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

    def get_cnt(self):
        """集合の個数を求める"""
        return self.cnt


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]


uf = UnionFind(n)
for u, v in edges:
    u -= 1
    v -= 1
    uf.merge(u, v)

ans = 0
for i in range(n):
    ans = max(uf.get_size(i), ans)
print(ans)