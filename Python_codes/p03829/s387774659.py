from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,a,b = inpl()
x = inpl()
res = 0
for i in range(n-1):
    if (x[i+1] - x[i])*a > b:
        res += b
    else:
        res += (x[i+1] - x[i])*a
print(res)