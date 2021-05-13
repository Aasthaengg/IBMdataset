from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

a,b,c,d,e,f = inpl()
mx = 0
res = 0
ans = 0
for i in range(40):
    for j in range(40):
        water = 100*a*i + 100*b*j
        if water == 0:
            continue
        for k in range(300):
            for l in range(300):
                sugar = c*k + d*l
                if water+sugar > f or sugar > (a*i+b*j)*e:
                    continue
                if sugar/(water+sugar) >= mx:
                    mx = sugar/(water+sugar)
                    res = water+sugar
                    ans = sugar
print(res,ans)