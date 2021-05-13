from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime,random
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())

A,B,K = inpl()
taka = True

for i in range(K):
    if taka:
        A -= A%2
        A,B = A//2,B+A//2
    else:
        B -= B%2
        B,A = B//2,A+B//2

    taka = not taka

print(A,B)
