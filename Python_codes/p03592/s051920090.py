from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m,k = inpl()
for i in range(n+1):
    for j in range(m+1):
        now = i*m+j*n-i*j*2
        if now == k:
            print('Yes')
            quit()
print('No')