from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = inpl()
b = inpl()
c = inpl()
a.sort()
b.sort()
c.sort()
lb = [0] * n
res = 0
for i in range(n):
    tmp = bisect.bisect_right(b,a[i])
    if tmp == n: continue
    lb[tmp] += 1
llb = list(itertools.accumulate(lb))
# print(lb,llb)
rr = [0] * n
for i in range(n):
    tmp = bisect.bisect_right(c,b[i])
    if tmp == n: continue
    rr[tmp] += llb[i]
print(sum(list(itertools.accumulate(rr))))