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
a = inpl()
d = defaultdict(int)
for i,x in enumerate(a):
    d[i+1-x] += 1
res = 0
for i,x in enumerate(a):
    res += d[i+1+x]
print(res)