from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 998244353
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N,H,W = inpl()
ans = 0
for _ in range(N):
    A,B = inpl()
    if H <= A and W <= B:
        ans += 1

print(ans)
