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

H, N = map(int, readline().split())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, readline().split())

MAX = 10 ** 10
dp = [MAX] * (H + 1)
dp[0] = 0
for i in range(N):
    for h in range(1, H + 1):
        if A[i] >= h:
            dp[h] = min(dp[h], B[i])
        else:
            dp[h] = min(dp[h], dp[h - A[i]] + B[i])
print(dp[H])
