import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

H,W = I()
maze = [list(s()) for _ in range(H)]
ans = [[0]*(W-1) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
            cnt = 0
            Flag1 = 0
            Flag2 = 0
            Flag3 = 0
            Flag4 = 0
            if i != 0:
                if maze[i-1][j] == '#':
                    cnt += 1
                Flag1 = 1
            if i != H-1:
                if maze[i+1][j] == '#':
                    cnt += 1
                Flag2 = 1
            if j != 0:
                if maze[i][j-1] == '#':
                    cnt += 1
                Flag3 = 1
            if j != W-1:
                if maze[i][j+1] == '#':
                    cnt += 1
                Flag4 = 1
            if Flag1 == Flag3 == 1:
                if maze[i-1][j-1] == '#':
                    cnt += 1
            if Flag1 == Flag4 == 1:
                if maze[i-1][j+1] == '#':
                    cnt += 1
            if Flag2 == Flag3 == 1:
                if maze[i+1][j-1] == '#':
                    cnt += 1
            if Flag2 == Flag4 == 1:
                if maze[i+1][j+1] == '#':
                    cnt += 1
            maze[i][j] = str(cnt)
for m in maze:
    print(''.join(m))