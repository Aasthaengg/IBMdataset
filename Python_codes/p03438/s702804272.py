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
res = 0
for x,y in zip(a,b):
    if x > y:
        res += x-y
    elif x < y:
        res -= (y-x)//2
# print(res)
print('No' if res > 0 else 'Yes')