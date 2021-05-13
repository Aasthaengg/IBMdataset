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

n,m=map(int,input().split())
abc=[list(map(int,input().split())) for i in range(m)]

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

# n,w = map(int,input().split()) #n:頂点数　w:辺の数
dic=defaultdict(int)
d = [[float("inf") for i in range(n)] for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(m):
    x,y,z = abc[i]
    x,y=x-1,y-1
    d[x][y] = z
    d[y][x] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
tmp=warshall_floyd(d)

for i in range(m):
    a,b,c=abc[i]
    if tmp[a-1][b-1]==c:
        dic[(a,b)]+=1

print(m-len(dic))