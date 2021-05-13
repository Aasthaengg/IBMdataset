from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = 26
D = inp()
c = inpl()
s = [inpl() for _ in range(D)]
last = [0] * n
res = [-1] * D
for d in range(D):
    ans = -1
    mx = -INF
    for i in range(n):
        now = s[d][i]
        for j in range(n):
            if i == j: continue
            now -= s[d][j] * (last[j]+1)
        if now > mx:
            mx = now
            ans = i
    res[d] = ans+1
    for j in range(n):
        last[j] += 1
        if j == ans: last[j] = 0
for x in res:
    print(x)