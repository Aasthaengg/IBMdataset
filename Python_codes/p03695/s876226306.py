from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = inpl()
bo = [False] * 8
free = 0
for x in a:
    now = x//400
    if now < 8:
        bo[now] = True
    else:
        free += 1
mi = sum(bo) if sum(bo) > 0 else 1
print(mi, sum(bo) + free)