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

H, W, N = map(int, input().split())
X = (H - 2) * (W - 2)

A = defaultdict(int)
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for p in range(3):
        for q in range(3):
            k, l = a - p, b - q
            if k < 0 or k >= H or l < 0 or l >= W:
                continue
            if k + 2 >= H or l + 2 >= W:
                continue
            A[(k, l)] += 1

ans = [0] * 10
for k, v in A.items():
    ans[v] += 1
ans[0] = X - sum(ans)

for a in ans:
    print(a)