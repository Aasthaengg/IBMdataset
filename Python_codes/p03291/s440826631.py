from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

s = input()
n = len(s)
dp = [[0] * 4 for _ in range(n+1)]
dp[0][0] = 1
for i,x in enumerate(s):
    for j in range(4):
        if x == '?':
            dp[i+1][j] = dp[i][j] * 3
        else:
            dp[i+1][j] = dp[i][j]
    if x == 'A' or x == '?':
        dp[i+1][1] += dp[i][0]
    if x == 'B' or x == '?':
        dp[i+1][2] += dp[i][1]
    if x == 'C' or x == '?':
        dp[i+1][3] += dp[i][2]
    for j in range(4):
        dp[i+1][j] %= mod
print(dp[-1][-1])