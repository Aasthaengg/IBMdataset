from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,k = inpl()
a = inpl()
ln = max(len(bin(max(a))), len(bin(k))) - 2
c = [0] * ln
res = 0
for x in a:
    for i in range(ln):
        c[i] += (x>>i)%2
# print(c)
for i in range(ln)[::-1]:
    if c[i] < (n+1)//2:
        # print(i)
        now = pow(2,i)
        if res + now <= k:
            res += now
ans = 0
for x in a:
    ans += res^x
print(ans)