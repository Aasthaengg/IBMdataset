import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N, M, Q = map(int, input().split())

acc = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    l, r = map(int, input().split())
    acc[l][r] += 1
for i in range(1, N + 1):
    for j in range(1, N + 1):
        acc[i][j] += acc[i][j - 1]

for i in range(Q):
    p, q = map(int, input().split())
    ans = 0
    for i in range(p, q + 1):
        ans += acc[i][q]
    print(ans)
