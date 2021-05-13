import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
import copy
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]

n=int(input())
a=[list(map(int,input().split())) for i in range(n)]

def warshall_floyd(d,d2):
    #d[i][j]: iからjへの最短距離

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==k or j==k:
                    continue
                if d[i][j]>d[i][k] + d[k][j]:
                    print(-1)
                    quit()
                if d[i][j]==d[i][k] + d[k][j]:
                    d2[i][j]=1
                # d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


d = [[float("inf") for i in range(n)] for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
cnt=0
for i in range(n):
    for j in range(n):
        d[i][j]=a[i][j]
        cnt+=a[i][j]
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
# print(d)

d2 = [[0 for i in range(n)] for i in range(n)]
warshall_floyd(d,d2)
# print(d2)
cnt=0
for i in range(n):
    for j in range(n):
        if d2[i][j]==0:
            cnt+=d[i][j]
print(cnt//2)