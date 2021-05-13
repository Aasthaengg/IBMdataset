import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N, M = map(int, input().split())
prices = [0] * M
ks = [0] * M
for i in range(M):
    a, b = map(int, input().split())
    C = list(map(int, input().split()))
    prices[i] = a
    ks[i] = C

dp = [INF] * (1 << N)
dp[0] = 0
for i in range(M):
    key_bit = 0
    for k in ks[i]:
        key_bit |= 1 << (k - 1)
    for bit in range((1 << N) - 1, -1, -1):
        if dp[bit] != INF:
            nx_bit = bit | key_bit
            dp[nx_bit] = min(dp[nx_bit], dp[bit] + prices[i])
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])


