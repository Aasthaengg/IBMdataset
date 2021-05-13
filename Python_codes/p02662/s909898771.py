from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,copy
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

mod = 998244353
n,s = inpl()
a = inpl()
dp = [[0]*(s+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(s+1):
        dp[i+1][j] = dp[i][j] * 2
        if j - a[i] >= 0:
            dp[i+1][j] += dp[i][j-a[i]]
        dp[i+1][j] %= mod
# print(dp)
print(dp[-1][-1])