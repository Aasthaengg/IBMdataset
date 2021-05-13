# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:26:39 2019
D - 連結 / Connectivity
実行時間制限: 2 sec / メモリ制限: 256 MB

配点 : 
400 点
@author: justwah
"""
import sys

input = sys.stdin.readline # use this runtime 1523 ms> 1214ms

class UnionFind:
    def __init__(self, n):
        self.rank = [0]*n
        self.parent = [-1]*n
        self.n = n
        
    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
        
    def merge(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] +=1
                
    def same(self, a, b):
        return self.root(a) == self.roob(b)


n, k, l = map(int, input().split())

uf_road = UnionFind(n)
for _ in range(k):
    p, q = map(int, input().split())
    uf_road.merge(p-1, q-1)

uf_rail = UnionFind(n)
for _ in range(l):
    r, s = map(int, input().split())
    uf_rail.merge(r-1, s-1)
    
d = {}
IDs = [0]*n
for i in range(n):
    ID = (uf_road.root(i), uf_rail.root(i))
    IDs[i] = ID
    if ID in d:
        d[ID] += 1
    else:
        d[ID] = 1

ans = []
for i in range(n):
    ans.append(d[IDs[i]])
print(*ans)