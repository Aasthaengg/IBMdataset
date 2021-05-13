#!/usr/bin/env python
# -*- coding: utf-8 -*-


class UnionFind():
    """ UnionFindはグループの分割はできないことに注意 """
    def __init__(self, n):
        """
            n: 要素数
            parents: 親を示す、-1の場合、自身の親がいない(頂点)であることを示す
        """
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """
        親の要素が何かを調べる
        同じ要素であれば、同じグループに所属することを示す
        探索しながら、親を頂点につなぎ直すことで、効率的にまとめることができる
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        xとyの所属するグループをまとめる
        """
        x = self.find(x)
        y = self.find(y)

        # 同じ親だった場合、既にグループはまとまっているので処理を終了する
        if x == y:
            return

        # 浅い方を深い方に繋ぐようにする
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def most_depth_root(self):
        return -min(self.parents)


N, M = map(int, input().split())

union_find = UnionFind(N)
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    union_find.union(x, y)

print(union_find.most_depth_root())