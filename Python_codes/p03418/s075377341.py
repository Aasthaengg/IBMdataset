from collections import Counter,defaultdict,deque
from heapq import heapify,heappop,heappush
import sys,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,k = inpl()
res = 0
if k == 0:
    res = n**2
else:
    for i in range(k+1,n+1):
        res += (i - k)*((n+1) // i)
        t = n % i
        if t == i-1:
            continue
        if t >= k:
            res += t-k+1
print(res)

    
