import bisect
import collections
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7

N,M = map(int,(input().split()))
dp = [float("inf")]*(2**N)
dp[0] = 0
for i in range(M):
    a,b = map(int,(input().split()))
    c = list(map(int,(input().split())))
    d = 0
    for j in c:
        d += 2**(j-1)
    for j in range(2**N):
        dp[j|d] = min(dp[j|d],dp[j]+a)

ans = dp[-1]
if ans != float("inf"):
    print(ans)
else:
    print(-1)