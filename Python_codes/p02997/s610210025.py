from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,pprint,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,k = inpl()

if k > (n-1)*(n-2)//2:
    print(-1)
    quit()
res = []
for i in range(n-1):
    res.append([1,2+i])
l = (n-1)*(n-2)//2 - k

ind = 2

def p():
    m = len(res)
    print(m)
    for i in range(m):
        print(*res[i])
if l == 0 :
    p(); quit()
for i in range(ind,n):
    for j in range(i+1,n+1):
        res.append([i,j])
        l -= 1
        if l == 0:
            p()
            quit()
    ind += 1
