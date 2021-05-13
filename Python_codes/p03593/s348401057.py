from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

h,w = inpl()
cnt = defaultdict(int)
for _ in range(h):
    for x in input():
        cnt[x] += 1
one = two = 0
for va in cnt.values():
    now = va%4
    if now == 1 or now == 3:
        one += 1
    if now == 2 or now == 3:
        two += 1
res = False
if h%2 == 0 and w%2 == 0:
    if not one and not two:
        res = True
elif h%2 and w%2:
    if one == 1 and two <= (w-1)//2 + (h-1)//2:
        res = True
else:
    now = h if w%2 else w
    if not one and two <= now//2:
        res = True
print('Yes' if res else 'No')