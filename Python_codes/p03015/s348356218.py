from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

L = input()
n = len(L)
#0:kaku 1:mikaku
dp = [[0] * (n+1) for _ in range(2)]
dp[1][0] = 1
for i,x in enumerate(L):
    if x == '0':
        dp[0][i+1] = dp[0][i]*3
        dp[1][i+1] = dp[1][i]
    else:
        dp[0][i+1] = dp[0][i]*3 + dp[1][i]
        dp[1][i+1] = dp[1][i]*2
    dp[0][i+1] %= mod
    dp[1][i+1] %= mod
print((dp[0][-1] + dp[1][-1])%mod)
