# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:46:45 2020

@author: liang
"""


class UnionFind():
    def __init__(self, N):
        self.N = N
        self.par = [-1]*N
    
    def find(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return self
        if self.par[a] > self.par[b]:
            a, b = b, a
        self.par[a] += self.par[b]
        self.par[b] = a
    
    def same(self, a, b):
        a = self.find(a)
        b = self.find(b)
        return a == b
    
N, M = map(int, input().split())
uf = UnionFind(N)
for i in range(M):
    a, b = map(int,input().split())
    uf.union(a-1, b-1)

ans = -min(uf.par)
print(ans)  