from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
s = [input() for i in range(2)]
prev = 0 #0:横 1:縦
if s[0][0] == s[1][0]:
    res = 3
    i = 1
    prev = 1
else:
    res = 6
    i = 2
while i < n:
    if s[0][i] == s[1][i]:
        if prev:
            res = (res*2) % mod
        i += 1
        prev = 1
    else:
        if prev:
            res = (res*2) % mod
        else:
            res = (res*3) % mod
        i += 2
        prev = 0
print(res)