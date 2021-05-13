from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,copy
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = []
for _ in range(n):
    tmp = inpl()
    tmp = [x-1 for x in tmp] + [-1]
    # print(tmp)
    a.append(deque(tmp))
md = [0] * n
nx = [-1] * n
for i in range(n):
    nx[i] = a[i].popleft()
q = deque(range(n))

while q:
    x = q.popleft()
    y = nx[x]
    if nx[y] == x:
        d = max(md[x], md[y])
        md[x] = md[y] = d+1
        nx[x] = a[x].popleft()
        nx[y] = a[y].popleft()
        q.append(x); q.append(y)
if any(x for x in a):
    print(-1)
else:
    print(max(md))