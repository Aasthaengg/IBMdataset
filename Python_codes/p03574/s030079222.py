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
H,W = LI()
S = [list(_S()) for _ in range (H)]

# ans = np.zeros(shape=(H,W))
def replace(x, y):
    # 移動する8方向をループ
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            # x, y 方向それぞれに dx, dy 移動した場所を (nx, ny) とする
            nx = x + dx
            ny = y + dy

            if 0 <= nx and nx < H and 0 <= ny and ny < W and S[nx][ny] == "#":
                count += 1
    S[x][y]=str(count)


for i in range(H):
    for j in range(W):
        if not (S[i][j] == "#"):
            replace(i,j)

for row in S:
  print(*row,sep='')