import math
import numpy as np
import sys
import os
from operator import mul

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353    

# grid
# N = I()
# 黒く塗りつぶす#が独立していたら不可
H,W = LI()
S = [list(_S()) for _ in range (H)]

def check(x, y):
    # 移動する4方向をループ
    res = False
    # for dx,dy in itertools.product([-1,0,1],repeat=2):
    dxs = [-1,1]
    dys = [-1,1]
    for dx in dxs:
        nx = x + dx
        ny = y
        if 0 <= nx and nx < H and S[nx][ny] == "#":
            res = True
    for dy in dys:
        nx = x
        ny = y + dy
        if 0 <= ny and ny < W and S[nx][ny] == "#":
            res = True
    return res

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            if not check(i,j):
                print('No')
                exit()

print('Yes')