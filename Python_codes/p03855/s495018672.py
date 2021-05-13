# 参考URL https://note.nkmk.me/python-union-find/
class UnionFind():
    # parents
    # 各要素の親要素の番号を格納するリスト
    # 要素が根（ルート）の場合は-(そのグループの要素数)を格納する
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # find(x)
    # 要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # union(x, y)
    # 要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # size(x)
    # 要素xが属するグループのサイズ（要素数）を返す
    def size(self, x):
        return -self.parents[self.find(x)]

    # same(x, y)
    # 要素x, yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # members(x)
    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # roots()
    # すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # group_count()
    # グループの数を返す
    def group_count(self):
        return len(self.roots())

    # all_group_members
    # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    # __str__()
    # print()での表示用
    # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

import sys
def input():
    return sys.stdin.readline().strip()

n, k, l = map(int, input().split())

road = UnionFind(n)
rail = UnionFind(n)
for _ in range(k):
    p, q = map(int, input().split())
    road.union(p-1, q-1)
for _ in range(l):
    r, s = map(int, input().split())
    rail.union(r-1, s-1)

dic = {}
l = []
for i in range(n):
    tup = (road.find(i), rail.find(i))
    l.append(tup)
    if tup in dic:
        dic[tup] += 1
    else:
        dic[tup] = 1

ans = []
for i in l:
    ans.append(dic[i])

print(' '.join(map(str, ans)))