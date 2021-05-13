from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = list(map(float,input().split()))
dp = [[0] * (n+5) for i in range(n+5)]
dp[0][0] = 1
for i in range(n):
    for j in range(n+1):
        if j == 0:
            dp[i+1][j] = dp[i][j] * (1-a[i])
            continue
        dp[i+1][j] = dp[i][j-1] * a[i] + dp[i][j] * (1-a[i])
print(sum(dp[n][n//2+1:]))
# pprint.pprint(dp)