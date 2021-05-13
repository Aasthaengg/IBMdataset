import sys
import itertools
# import numpy as np
import time
import math
import heapq
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
INF = 10 ** 9 + 7

# map(int, input().split())
# list(map(int, input().split()))

N, M = map(int, input().split())
A = set()
for i in range(M):
    a = int(input())
    A.add(a)


dp = [0] * (N + 1)
dp[0] = 1
if not 1 in A:
    dp[1] = 1
for i in range(2, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % INF
    if i in A:
        dp[i] = 0
print(dp[N])
# ans = 1
# cur = 0
# for a in A:
#     steps = (a - 1) - cur
#     cur = a + 1
