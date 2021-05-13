from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

s = input()[::-1]
n = len(s)
now = [0] * 13
now[0] = 1
for i,x in enumerate(s):
    new = [0] * 13
    c = pow(10,i,13)
    if x == '?':
        for k in range(10):
            for j in range(13):
                new[(j+c*k)%13] += now[j]
                new[(j+c*k)%13] %= mod
    else:
        for j in range(13):
            new[(j+c*int(x))%13] += now[j]
            new[(j+c*int(x))%13] %= mod
    now = new[::]
print(now[5])