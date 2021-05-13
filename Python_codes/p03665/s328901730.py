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

N, P = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * 5005
dp[0] = 1

for a in A:
    for i in range(5000, 0, -1):
        if i - a >= 0:
            dp[i] += dp[i - a]

print(sum(dp[i] for i in range(len(dp)) if i % 2 == P))