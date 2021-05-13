from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def err():
    print('No')
    quit()
def ok():
    print('Yes')
    quit()

n = inp()
a = inpl()
a.sort()
c = Counter(a)
now = a[0]
for i in range(1,n):
    now ^= a[i]
if now: err()
if a[0] == a[-1] == 0: ok()
if n == 3:
    x,y,z = a
    if x == 0 and y == z: ok()
if n%3: err()
if len(c.keys()) == 3:
    for x in c.values():
        if x != n//3:
            err()
    x,y,z = c.keys()
    if x^y != z:
        err()
elif len(c.keys()) == 2:
    x,y = sorted(list(c.values()))
    if x != n//3 or y != n//3*2:
        err()
    x,y = sorted(list(c.keys()))
    if x != 0: err()
else: err()
ok() 
