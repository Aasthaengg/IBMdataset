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
a.sort(reverse = True)
cnt = n
ind = 0
res = 0
while cnt:
    if ind % 2:
        res += a[ind]
        cnt -= 1
    ind += 1
print(res)