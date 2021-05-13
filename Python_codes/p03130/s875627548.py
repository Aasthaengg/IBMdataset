from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

z = []
for i in range(3):
    a,b = inpl()
    z.append(a)
    z.append(b)
c = Counter(z)
for key in c.keys():
    if c[key] > 2:
        print('NO')
        break
else:
    print('YES')
