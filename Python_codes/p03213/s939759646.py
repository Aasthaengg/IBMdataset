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

N = int(readline())

dp = [0] * (N + 1)

for i in range(1, N + 1):
    x = i
    for j in range(2, i):
        while x % j == 0:
            x //= j
            dp[j] += 1
    if x != 1:
        dp[x] += 1
# dp = sorted(dp, reverse=True)

ans = 0
ans += any(x for x in dp if x >= 74)

x = 0
y = 0
for i in range(N + 1):
    if dp[i] >= 24:
        x += 1
    if dp[i] >= 2:
        y += 1
ans += x * (y - 1)

x = 0
y = 0
for i in range(N + 1):
    if dp[i] >= 14:
        x += 1
    if dp[i] >= 4:
        y += 1
ans += x * (y - 1)

x = 0
y = 0
z = 0
for i in range(N + 1):
    if dp[i] >= 4:
        x += 1
        y += 1
    if dp[i] >= 2:
        z += 1
ans += x * (y - 1) * (z - 2) // 2
# print(dp)
# print(x, y, z)

print(ans)