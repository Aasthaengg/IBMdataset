#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from math import gcd
from operator import add, itemgetter, mul, xor
def cmb(n,r,mod):
  bunshi=1
  bunbo=1
  for i in range(r):
    bunbo = bunbo*(i+1)%mod
    bunshi = bunshi*(n-i)%mod
  return (bunshi*pow(bunbo,mod-2,mod))%mod
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

h,w = MI()
a = [list(input()) for i in range(h)]
d = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dist = [[-1]*w for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            d.append([i,j])
            dist[i][j] = 0
while d:
    s = d.popleft()
    x= s[0]
    y= s[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue
        else:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                ans = max(ans,dist[nx][ny])
                d.append([nx,ny])

print(ans)
