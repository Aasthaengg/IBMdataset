from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
a = inpl()
res = 0
for i in range(n-1):
    if a[i+1] + a[i] > m:
        r = a[i+1] + a[i] - m
        res += r
        if a[i] <= m:
            a[i+1] -= r
        else:
            a[i+1] = 0
            a[i] = m
print(res)         