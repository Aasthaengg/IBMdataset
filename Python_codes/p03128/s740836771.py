from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
a = sorted(inpl(), reverse = True)
b = [0,2,5,5,4,5,6,3,7,6]
dp = [0] * (n+1)

for i in a:
    w,v = b[i],i
    for j in range(n+1):
        if j < w:
            continue
        if j%w == 0 or dp[j-w]:
            dp[j] = max(dp[j], dp[j-w]*10 + v)
    # print(dp)
print(dp[-1])