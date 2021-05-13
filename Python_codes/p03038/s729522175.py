from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
a = inpl()
a.sort()
bc = [inpl() for _ in range(m)]
bc.sort(key=lambda x:x[1], reverse = True)
ind = -1
now = -1
cnt = 0
for i in range(n):
    if cnt == 0:
        ind += 1
        if ind >= m: break
        cnt, now = bc[ind]
    if a[i] >= now:
        break
    a[i] = now
    cnt -= 1
print(sum(a))