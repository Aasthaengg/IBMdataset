from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = inpl()
b = inpl()
res = 0
for i in range(n):
    if a[i] > b[i]:
        res += b[i] - a[i]
    elif b[i] - a[i]:
        res += (b[i] - a[i])//2
print('Yes' if res >= 0 else 'No')