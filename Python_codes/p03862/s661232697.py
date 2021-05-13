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

N, x = map(int, input().split())
A = list(map(int, input().split()))

total = 0
goal = x * (N - 1)
for i in range(N):
    if i == 0 or i == N - 1:
        total += A[i]
    else:
        total += 2 * A[i]

if total <= goal:
    print(0)
    exit()

ans = 0
if A[0] > x:
    diff = A[0] - x
    ans += diff
    A[0] -= diff
# if A[N - 1] > x:
#     diff = A[N - 1] - x
#     ans += diff
#     A[N - 1] -= diff

for i in range(1, N):
    if A[i - 1] + A[i] > x:
        diff = (A[i - 1] + A[i]) - x
        A[i] -= diff
        ans += diff
print(ans)



