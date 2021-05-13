from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = [input() for i in range(3)]
res = 0
for i in range(n):
    if a[0][i] == a[1][i] == a[2][i]:
        continue
    if a[0][i] == a[1][i] or a[2][i] == a[1][i] or a[0][i] == a[2][i]:
        res += 1
    else:
        res += 2
print(res)