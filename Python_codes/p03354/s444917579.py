n, m = (int(x) for x in input().split())
P = list(int(x) for x in input().split())
XY = [tuple(int(x) for x in input().split()) for _ in range(m)]

class UnionFind:
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
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    """
    n個の要素を0 ~ n - 1の番号で管理する。以下の属性およびメソッドを持つ。

    parents
    各要素の親要素の番号を格納するリスト
    要素が根（ルート）の場合は-(そのグループの要素数)を格納する

    find(x)
    要素xが属するグループの根を返す

    union(x, y)
    要素xが属するグループと要素yが属するグループとを併合する

    size(x)
    要素xが属するグループのサイズ（要素数）を返す

    same(x, y)
    要素x, yが同じグループに属するかどうかを返す

    members(x)
    要素xが属するグループに属する要素をリストで返す

    roots()
    すべての根の要素をリストで返す

    group_count()
    グループの数を返す

    all_group_members
    {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す

    __str__()
    print()での表示用
    ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    """

uf = UnionFind(n+1)
for x, y in XY:
    uf.union(x, y)

ans = 0
for i, p in enumerate(P, start=1):
    if uf.same(i, p):
        ans += 1
print(ans)