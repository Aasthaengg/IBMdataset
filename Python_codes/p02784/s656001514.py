import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

H,N = LI()
A = LI()

A_np = np.array(A)
A_sum = np.sum(A_np)

ans = True
if H>A_sum:
    ans=False

if ans:
    print('Yes')
else:
    print('No')
