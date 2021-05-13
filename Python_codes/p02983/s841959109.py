from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

l,r = inpl()
if r-l > 2019:
    print(0)
else:
    res = INF
    for i in range(l,r):
        for j in range(i+1,r+1):
            res = min(res, (i*j)%2019)
    print(res)