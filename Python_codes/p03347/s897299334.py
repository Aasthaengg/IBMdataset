from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = [inp() for _ in range(n)]
res = 0
for i in range(1,n)[::-1]:
    if a[i]-a[i-1] == 1:
        res += 1
    else:
        res += a[i]
for i in range(n-1):
    if a[i+1] - a[i] > 1:
        res = -1
if a[0] != 0:
    res = -1 
print(res)