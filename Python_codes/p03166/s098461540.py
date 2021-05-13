import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
# from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1)


    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def union(self, x, y, w=1):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

n,m=map(int,input().split())
xy=[list(map(int,input().split())) for i in range(m)]

edgenum=[0]*(n+1)
edge=[[] for i in range(n+1)]

for i in range(m):
    x,y=xy[i]
    edgenum[x]+=1
    edge[y].append(x)
# print(edgenum)
# print(edge)

d=deque()
itta=[0]*(n+1)
for i in range(n):
    i+=1
    if edgenum[i]==0:
        d.append(i)
# print(d)

while d:
    now=d.popleft()
    # print(itta,now)
    # print(edgenum)

    for i in edge[now]:
        edgenum[i]-=1
        if edgenum[i]==0:
            d.append(i)
            itta[i]=max(itta[i],itta[now]+1)
# print(itta)
print(max(itta))