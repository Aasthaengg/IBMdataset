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
A = [list(map(int, input().split())) for _ in range(H)]

path = []
for i in range(H):
    if i % 2 == 0:
        for j in range(W):
            x = (i, j)
            path.append(x)
    else:
        for j in range(W - 1, -1, -1):
            x = (i, j)
            path.append(x)

ans = []
for i in range(len(path) - 1):
    p = path[i]
    p2 = path[i + 1]
    if A[p[0]][p[1]] % 2 != 0:
        A[p2[0]][p2[1]] += 1
        ans.append((p[0] + 1, p[1] + 1, p2[0] + 1, p2[1] + 1))
print(len(ans))
for a in ans:
    print(*a)

