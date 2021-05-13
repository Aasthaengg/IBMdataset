from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

h,w,a,b = inpl()
for i in range(h):
    res = []
    tmp = 0 if i < b else 1
    for j in range(w):
        if j < a:
            res.append(str(tmp))
        else:
            res.append(str(tmp^1))
    print(''.join(res))