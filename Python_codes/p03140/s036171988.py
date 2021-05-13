from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N = inp()
A = input()
B = input()
C = input()

ans = 0
for i in range(N):
    a,b,c = A[i],B[i],C[i]
    L = len(set([a,b,c]))
    ans += L-1

print(ans)
