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

N, K = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))
C = list(map(int, input().split()))


ans = -INF
for i in range(N):
    nx = i
    total = 0
    L = [] 
    while True:
        nx = P[nx]
        total += C[nx]
        L.append(C[nx])
        if nx == i:
            break
    l = len(L)
    tmp = 0
    for j in range(l):
        if j + 1 > K:
            break
        tmp += L[j]
        now = tmp
        if total > 0:
            e = (K - j - 1) // l
            now += total * e
        ans = max(ans, now)
    # if total > 0:
    #     now = total * (K // l)
    #     ans = max(ans, now)
    #     r = K % l
    #     for j in range(r):
    #         now += L[j]
    #         ans = max(ans, now)
print(ans)


