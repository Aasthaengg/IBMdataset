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