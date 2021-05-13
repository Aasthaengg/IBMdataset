#!/usr/bin/env python3
n = int(input())
A = [int(x) for x in input().split()]
A.sort()
s = 0
for i in range(n-1):
    s += A[i]
if A[-1] < s:
    print('Yes')
else:
    print('No')