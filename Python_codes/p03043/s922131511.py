from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


n,k = inpl()
res = 0
for i in range(1,n+1):
    cnt = 0
    now = i
    if i > k:
        res += 1/n
        continue
    while now < k:
        now *= 2
        cnt += 1
    res += 1/n*(1/2**cnt)
print(res)