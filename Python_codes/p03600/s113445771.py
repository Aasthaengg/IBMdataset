from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = [inpl() for _ in range(n)]
res = 0
fin = set()
for k in range(n):
    for i in range(n):
        for j in range(n):
            d = a[i][k] + a[k][j]
            if a[i][j] > d:
                print(-1)
                quit()
            if a[i][j] == d and i != k and j != k:
                fin.add((i,j))

for i in range(n):
    for j in range(i+1,n):
        if (i,j) in fin: continue
        res += a[i][j]
print(res)