from bisect import bisect_right
from itertools import accumulate

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

A.sort()
B.sort()
C.sort()

# a < b < c

# Bcnt[i]: B[i]が置ける下部パーツの数
Bcnt = [0] * N
for i,b in enumerate(B):
    r = bisect_right(C, b)
    Bcnt[i] = N - r
 
Bcnt = [0] + list(accumulate(Bcnt))
 
Acnt = [0] * N
for i,a in enumerate(A):
    r = bisect_right(B, a)
    Acnt[i] = Bcnt[N] - Bcnt[r]

print(sum(Acnt))