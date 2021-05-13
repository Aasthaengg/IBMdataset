import sys
import itertools
# import numpy as np
import time
import math
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
 
from functools import reduce
# from math import *
from fractions import *
H, W = map(int, readline().split())
S = [0 for i in range(H)]
for i in range(H):
    S[i] = readline().decode().strip()
 
from collections import deque
def bfs(start, H, W):
    INF = 10 ** 9
    visited = [False] * (H * W)
    q = deque([(start[0], start[1], 0)])
    max_d = 0
    while q:
        (i, j, d) = q.popleft()
        max_d = max(max_d, d)
        if visited[i * W + j]:
            continue
        visited[i * W + j] = True
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx * dy != 0:
                    continue
                if dx == dy:
                    continue
                if i + dy < 0 or i + dy >= H or j + dx < 0 or j + dx >= W:
                    continue
                if S[i + dy][j + dx] == '#':
                    continue
                if visited[(i + dy) * W + j + dx]:
                    continue
                q.append((i + dy, j + dx, d + 1))
    return max_d
 
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        start = (i, j)
        ans = max(ans, bfs(start, H, W))
print(ans)