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
t = input()
for i in range(n):
    for j in range(n-i):
        if s[i+j] != t[j]:
            break
    else:
        print(n+i)
        break
else:
    print(n*2)