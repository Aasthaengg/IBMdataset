from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = [inpl() for _ in range(n)]
if n == 1:
    print(1)
    quit()
c = []
for i,(x,y) in enumerate(a):
    for j,(z,w) in enumerate(a):
        if i == j: continue
        c.append(((x-z), (y-w)))
h = Counter(c)
print(n-max(h.values()))
