"""
Union Find 木クラス
参考URL：https://note.nkmk.me/python-union-find/

parents
各要素の親要素の番号を格納するリスト
要素が根（ルート）の場合は-(そのグループの要素数)を格納する
例：
    parents[2] = 0 → 要素2の親は0
    parents[0] = -3 → 要素0は根であり、そのグループの要素数は3個
"""
class UnionFind():
    # 初期化（初期状態は全要素が根）
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # xの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # 経路圧縮も同時に行う
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        # 根が同じならx,yは既に同じグループ
        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 要素xが属するグループのサイズ（要素数）を返す
    def size(self, x):
        return -self.parents[self.find(x)]

    # 要素x, yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # グループの数を返す
    def group_count(self):
        return len(self.roots())

    # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    # print()での表示用
    # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

n, m = map(int, input().split())
u = UnionFind(n)
for i in range(m):
    a, b = map(int, input().split())
    u.union(a-1, b-1)

print(u.group_count() - 1)