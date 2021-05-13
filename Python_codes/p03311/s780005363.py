#coding: utf-8

import math

N = int(input())
A = [int(n) for n in input().split()]
for i in range(len(A)):
    A[i] -= (i+1)
A.sort()

med = 0
if N % 2 == 0:
    m1 = N // 2
    m2 = m1 - 1
    med = round((A[m1] + A[m2]) / 2)
else:
    m1 = (N+1) // 2
    med = A[m1-1]

sad = sum([abs(a-med) for a in A])

print(sad)

