import math
import sys
import os
from operator import mul
import collections
import itertools
import numpy as np
import copy

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")

H,W,K = LI()
grid = [list(_S()) for i in range(H)]
ans = 0

for x in range(1<<H):
    for y in range(1<<W):
        count = 0
        for i in range(H):
            for j in range(W):
                # 塗りつぶされない
                if (x >> i) & 1 == 0 and (y >> j) &1 ==0:
                    if grid[i][j] == '#':
                        count += 1
        if count == K:
            ans += 1

print(ans)