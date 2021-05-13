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
now = 0
res = INF
cnt = 0
for i in range(n):
    now += a[i]
    if i%2 == 0:
        if now <= 0:
            cnt += 1-now
            now = 1
    else:
        if now >= 0:
            cnt += now+1
            now = -1
    # print(i,now,cnt)
res = min(res,cnt)
now = 0
cnt = 0
for i in range(n):
    now += a[i]
    if i%2:
        if now <= 0:
            cnt += -now + 1
            now = 1
    else:
        if now >= 0:
            cnt += now + 1
            now = -1
    # print(i,now,cnt)    
res = min(res,cnt)
print(res)