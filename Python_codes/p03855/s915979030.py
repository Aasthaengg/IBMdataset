from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import permutations,combinations
from collections import defaultdict,Counter
from pprint import pprint

def myinput():
    return map(int,input().split())

def mycol(data,col):
    return [ row[col] for row in data ]

def mysort(data,col):
    data.sort(key=lambda x:x[col],reverse=False)
    return data

def mymax(data):
    M = -1*float("inf")
    for i in range(len(data)):
        m = max(data[i])
        M = max(M,m)
    return M

def mymin(data):
    m = float("inf")
    for i in range(len(data)):
        M = min(data[i])
        m = min(m,M)
    return m

class UnionFind():
    # parentsは「要素が根の場合に"そのグループの要素数*(-1)"を格納するリスト」
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    # 要素xが属するgroupの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    # 要素xが属するgroupと要素yが属するgroupを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
    # 要素xが属するgroupのサイズ（要素数）を返す
    def size(self, x):
        return -self.parents[self.find(x)]
    # 要素x,yが同じgroupに属するかをTrueかFalseで返す
    def same(self, x, y):
        return self.find(x) == self.find(y)
    # 要素xが属するgroupに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    # 全ての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    # groupの数を返す
    def group_count(self):
        return len(self.roots())
    # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

n,k,l = myinput()
pq = [ list(myinput()) for _ in range(k) ]
rs = [ list(myinput()) for _ in range(l) ]

uf1 = UnionFind(n)
for i in range(k):
    p = pq[i][0]
    q = pq[i][1]
    uf1.union(p-1,q-1)

uf2 = UnionFind(n)
for i in range(l):
    r = rs[i][0]
    s = rs[i][1]
    uf2.union(r-1,s-1)

d = defaultdict(lambda: 0)
# print(d)
for i in range(n):
    d[(uf1.find(i),uf2.find(i))] += 1
# print(d)
for i in range(n):
    ans = d[(uf1.find(i),uf2.find(i))]
    print(ans)