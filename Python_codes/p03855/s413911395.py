import itertools

class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * (size + 1)  # 非負なら親ノード，負ならグループの要素数

    def root(self, x):  # root(x): xの根ノードを返す．
        if self.parent[x] < 0:
            return x
        elif self.parent[self.parent[x]] < 0:
            return self.parent[x]
        else:
            self.parent[x] = self.root(self.parent[x])  # xをxの根に直接つなぐ
            return self.parent[x]

    def merge(self, x, y):  # merge(x,y): xのいるグループと$y$のいるグループをまとめる
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:  # xの要素数がyの要素数より「小さい」とき入れ替える
            x, y = y, x
        self.parent[x] += self.parent[y]  # xの要素数を更新
        self.parent[y] = x  # yをxにつなぐ
        return True

    def issame(self, x, y):  # same(x,y): xとyが同じグループにあるならTrue
        return self.root(x) == self.root(y)

    def size(self, x):  # size(x): xのいるグループの要素数を返す
        return -self.parent[self.root(x)]

import collections
N,K,L = list(map(int,input().split(" ")))
tree1 = UnionFind(N)
tree2 = UnionFind(N)
anss = collections.defaultdict(lambda :0)
querys = []
for _ in range(K):
    p,q = map(int,input().split(" "))
    tree1.merge(p,q)
for _ in range(L):
    r, s = map(int, input().split(" "))
    tree2.merge(r, s)

for i in range(1,N + 1):
    anss[(tree1.root(i),tree2.root(i))] += 1
temp = [0] * (N + 1)
for i in range(1,N + 1):
    temp[i] =  anss[(tree1.root(i),tree2.root(i))]
print(*temp[1:])

