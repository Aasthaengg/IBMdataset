from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

x,y,z,k = inpl()
a = inpl()
b = inpl()
c = inpl()
ab = []
for s in a:
    for t in b:
        ab.append(s+t)
ab.sort(reverse = True)
ab = ab[:3000]
abc = []
for s in ab:
    for j in c:
        abc.append(s+j)
abc.sort(reverse = True)
print(*abc[:k])
