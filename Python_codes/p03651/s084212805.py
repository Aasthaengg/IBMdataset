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
g = a[0]
for i in range(1,n):
    g = fractions.gcd(g,a[i])
if max(a) >= m and m % g == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')