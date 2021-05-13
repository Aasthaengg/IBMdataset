import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

H, W = map(int, input().split())
S = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        ok = False
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            y = i + dy
            x = j + dx
            if y < 0 or y >= H or x < 0 or x >= W:
                continue
            if S[i][j] == '.':
                ok = True
                continue

            if S[y][x] == '#':
                ok = True
        if not ok:
            print("No")
            exit()
print("Yes")

