from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

h1,m1,h2,m2,k = inpl()
if m1 > m2:
    m2 += 60
    h2 -= 1
print((h2-h1)*60+(m2-m1)-k)
