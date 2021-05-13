# import numpy as np
# import math
import sys
input = sys.stdin.readline

N = int(input())

T = []
A = []

for i in range(N):
    temp = list(map(int,input().split()))
    T.append(temp[0])
    A.append(temp[1])

for i in range(1,N):
    if (T[i-1] <= T[i]) & (A[i-1] <= A[i]):
        # print(T[i],A[i])
        continue
    else:
        rT = - ( - T[i-1] // T[i])
        rA = - ( - A[i-1] // A[i])
        temp = max(rT,rA)
        T[i] *= temp
        A[i] *= temp
        # print(T[i],A[i])

res = T[N-1] + A[N-1]

print(res)
