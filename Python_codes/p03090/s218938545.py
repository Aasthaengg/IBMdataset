from collections import Counter,defaultdict,deque
from bisect import bisect_left
import sys,math,itertools,pprint,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
tmp = n-1 if n%2 else n
m = (n**2 - (n+tmp))//2
print(m)
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j or i>j : continue
        if i+j == tmp+1: continue
        print(i,j)