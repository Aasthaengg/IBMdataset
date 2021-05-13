from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
from decimal import Decimal
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
wv = []
for i in range(m):
    a,b = inpl()
    cnt = 0
    c = inpl()
    for i in c:
        cnt += 1<<(i-1)
    wv.append((a,cnt))
dp = [INF for _ in range(1<<n)]
dp[0] = 0

for i in range(m):
    v,w = wv[i]
    for j in range(1<<n):
        dp[j|w] = min(dp[j|w], dp[j] + v)
print(dp[-1] if dp[-1] != INF else -1)