import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]

n,m,r=map(int,input().split())
r=list(map(int,input().split()))
abc=[list(map(int,input().split())) for i in range(m)]

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


d = [[float("inf") for i in range(n)] for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(m):
    x,y,z = abc[i]
    x-=1
    y-=1
    d[x][y] = z
    d[y][x] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
warshall_floyd(d)

lst=list(permutations(r))
# print(lst)

ans=float('inf')
for i in range(len(lst)):
    tmp=0
    for j in range(len(lst[i])-1):
        tmp+=d[lst[i][j+1]-1][lst[i][j]-1]
    ans=min(ans,tmp)
print(ans)