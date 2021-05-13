from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
ab = [input().split() for i in range(n)]
x = input()
res = 0
f = False
for i in range(n):
    a,b = ab[i]
    b = int(b)
    if a == x:
        f = True
        continue
    if f:
        res += b
print(res)