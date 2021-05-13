import os, sys, re, math
from functools import reduce

N = int(input())
A = [int(n) for n in input().split()]

v = 1
count = 0
for i in range(N):
    if A[i] == v:
        v += 1
    else:
        count += 1

if v > 1:
    print(count)
else:
    print(-1)
