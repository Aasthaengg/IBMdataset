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
c = Counter(a)
m = inp()
b = inpl()
d = Counter(b)
for key in list(d):
    if c[key] < d[key]:
        print('NO')
        break
else:
    print('YES')