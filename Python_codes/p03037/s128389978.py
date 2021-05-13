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

A = [0] * (N + 1)
for i in range(M):
    l, r = map(int, input().split())
    l -= 1
    A[l] += 1
    A[r] -= 1
for i in range(1, N):
    A[i] += A[i - 1]
ans = 0
for a in A:
    if a == M:
        ans += 1
print(ans)

