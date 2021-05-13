from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = inpl()
a.sort()
b = list(itertools.accumulate(a))
for i in range(n-1)[::-1]:
    if b[i]*2 < a[i+1]:
        res = n-i-1
        break
else:
    res = n
print(res)