import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * N
ex = [0] * N
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            cnt[i] += 1
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            ex[i] += 1

ans = 0
for i in range(N):
    ans += cnt[i] * ((K + 1) * K // 2) % MOD
for i in range(N):
    ans -= ex[i] * K
print(ans % MOD)