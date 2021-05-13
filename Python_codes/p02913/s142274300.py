from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,pprint,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
s = input()
dp = [[0 for i in range(n+5)] for j in range(n+5)]
res = 0
for i in range(n)[::-1]:
    for j in range(n)[::-1]:
        if i >= j: continue
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j+1] + 1
        else:
            dp[i][j] = 0
for i in range(n):
    for j in range(n):
        tmp = min(j-i, dp[i][j])
        res = max(res, tmp)
print(res)