import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import numpy as np

MOD = 10**9 + 7

N = int(input())
T = np.array(input().split(),dtype=np.int64)
A = np.array(input().split(),dtype=np.int64)

Tlower = T.copy()
Tlower[1:][T[1:]<=T[:-1]] = 1

A = A[::-1]
Alower = A.copy()
Alower[1:][A[1:]<=A[:-1]] = 1
A = A[::-1]; Alower = Alower[::-1]

lower = np.maximum(Alower,Tlower)
upper = np.minimum(A,T)
x = np.maximum(0,upper - lower + 1)

L = len(x); Lsq = int(L**.5+1)
x = np.resize(x,Lsq**2); x[L:] = 1; x = x.reshape((Lsq,Lsq))
for n in range(1,Lsq):
    x[:,n] *= x[:,n-1]; x[:,n] %= MOD
for n in range(1,Lsq):
    x[n] *= x[n-1,-1]; x[n] %= MOD
answer = x[-1,-1]
print(answer)