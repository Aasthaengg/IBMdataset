from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,pprint,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = inpl()
res = 1
cnt = [0,0,0]
for i in range(n):
    res *= cnt.count(a[i])
    res %= mod
    if res == 0: break
    cnt[cnt.index(a[i])] += 1
print(res)