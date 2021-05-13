from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,t = inpl()
wv = [inpl() for _ in range(n)]
wv.sort(key = lambda x:x[1],reverse = True)
res = 0
tmp = min(n,5)
for i in range(tmp):
    dp = [[0] * (t+5) for _ in range(n+5)]
    for j in range(n):
        w,v = wv[j]
        for k in range(t):
            if k < w or i == j:
                dp[j+1][k] = dp[j][k]
            else:
                dp[j+1][k] = max(dp[j][k], dp[j][k-w] + v)
    # print(dp[n][t-1])
    res = max(dp[n][t-1] + wv[i][1], res)
print(res)