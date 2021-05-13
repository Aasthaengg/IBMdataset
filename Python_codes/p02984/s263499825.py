#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

S = sum(A)

Ret = []
s = 0
for i in range(1, N, 2):
    s += A[i]

Ret.append(S-2*s)

for i in range(N-1):
    Ret.append(2*A[i]-Ret[-1])

print(*Ret)
