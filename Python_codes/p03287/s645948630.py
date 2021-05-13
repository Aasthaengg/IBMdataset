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
now = 0
p = defaultdict(int)
p[0] += 1
for i in range(n):
    now += a[i]
    p[now%m] += 1
res = 0
for key in list(p):
    res += p[key]*(p[key]-1)//2
print(res)