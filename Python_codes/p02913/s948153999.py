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
N = int(input())
S = input()
dp = [[0] * 5005 for _ in range(5005)]

for i in range(N - 1, -1, -1):
    for j in range(N - 1, -1, -1):
        if S[i] == S[j]:
            dp[i][j] = dp[i + 1][j + 1] + 1
ans = 0
for i in range(N):
    for j in range(N):
        if i >= j:
            continue
        now = min(dp[i][j], j - i)
        ans = max(now, ans)
print(ans)