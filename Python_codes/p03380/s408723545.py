#!/usr/bin/env python3

N = int(input())
A = sorted(list(map(int, input().split())))[::-1]

h = A[0]/2
r = 10**9
v = 0
for a in A[1:]:
    if r > abs(a-h):
        r = abs(a-h)
        v = a

print(str(A[0]) + ' ' + str(v))
