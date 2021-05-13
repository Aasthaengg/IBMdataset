from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

a,b = inpl()
res = 0
for x in range(a,b+1):
    tmp = str(x)
    if tmp == tmp[::-1]:
        res += 1
print(res)