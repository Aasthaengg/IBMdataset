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

N, M = map(int, input().split())
P = [[] for _ in range(N + 1)]
for i in range(M):
    p, y = map(int, input().split())
    P[p].append((y, i))

ans = [0] * M
for i in range(1, N + 1):
    if P[i] == 0:
        continue
    upper = ('0' * 5 + str(i))[-6:]
    A = sorted(P[i])
    for i, (_, j) in enumerate(A):
        lower = ('0' * 5 + str(i + 1))[-6:]
        ans[j] = upper + lower
        
for a in ans:
    print(a)

