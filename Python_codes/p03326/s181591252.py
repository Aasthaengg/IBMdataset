from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,m = inpl()
xyz = [inpl() for i in range(n)]
res = -INF
for bit in itertools.product(range(2),repeat=3):
    tmp = []
    for j in range(n):
        cnt = 0
        for i,b in enumerate(bit):
            if b == 0:
                cnt += xyz[j][i]
            else:
                cnt -= xyz[j][i]
        tmp.append(cnt)
    tmp.sort(reverse=True)
    res = max(res, sum(tmp[:m]))
print(res)