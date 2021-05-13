import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy
from operator import itemgetter

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces



H, W = na()
S = [ns() for _ in range(H)]
tmp = [[0] * W for _ in range(H)]

tmp2 = [[0] * W for _ in range(H)]
for i in range(H):
    ct = 0
    for j in range(W):
        if S[i][j] == '#':
            if ct != 0:
                for k in range(ct):
                   tmp[i][j-(k+1)] += ct 
            ct = 0
        else:
            ct += 1
    if ct != 0:
        for k in range(ct):
            tmp[i][j-k] += ct 
    

for j in range(W):
    ct = 0
    for i in range(H):
        if S[i][j] == '#':
            if ct != 0:
                for k in range(ct):
                   tmp[i-(k+1)][j] += ct - 1
            ct = 0
        else:
            ct += 1
    if ct != 0:
        for k in range(ct):
            tmp[i-k][j] += ct - 1

ans = -1
for i in range(H):
    for j in range(W):
        ans = max(ans, tmp[i][j])
print(ans)