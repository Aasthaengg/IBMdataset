#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

guusuu = []
kisuu = []

for i in range(N):
    if i % 2 == 0:
        guusuu.append(A[i])
    else:
        kisuu.append(A[i])

ret = []
if N % 2 == 0:
    ret = kisuu[::-1] + guusuu
else:
    ret = guusuu[::-1] + kisuu

print(' '.join(map(str, ret)))
