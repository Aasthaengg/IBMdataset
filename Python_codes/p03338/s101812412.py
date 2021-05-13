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
s = input()
res = 0
for i in range(n):
    a = s[:i]
    b = s[i:]
    ss = set(b)
    ans = 0
    sss = set()
    for x in a:
        if x in ss and not x in sss:
            ans += 1
        sss.add(x)
    res = max(res, ans)
print(res)