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
b = inpl()
p = []
m = 0
c = 0
for i in range(n):
    if a[i] - b[i] < 0:
        m += b[i]-a[i]
        c += 1
    elif a[i]-b[i] > 0:
        p.append(a[i] - b[i])
p.sort(reverse = True)
if m > sum(p):
    print(-1)
    quit()
for x in p:
    if m <= 0:
        break
    c += 1
    m -= x
print(c)

