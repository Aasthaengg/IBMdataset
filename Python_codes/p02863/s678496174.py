from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,t = inpl()
wv = sorted([inpl() for _ in range(n)])
dp = [[0]*t for _ in range(n+1)]

for i in range(n-1):
    w,v = wv[i]
    for j in range(t):
        if j < w:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j] , dp[i][j-w] + v)
res = 0
for i in range(n):
    tmp = dp[i][t-1] + wv[i][1]
    res = max(res, tmp)
print(res)