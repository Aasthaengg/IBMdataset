#!/usr/bin/env python3

from itertools import product
N = int(input())
A = {}
for i in range(N):
    A[i] = []

for i in range(N):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        A[i].append([x-1, y])

ret = -1
for p in product([0,1], repeat=N):
    cnt = 0
    flag = True
    for i in range(N):
        if p[i] == 1:
            for XY in A[i]:
                if XY[1] != p[XY[0]]:
                    flag = False
    if flag:
        ret = max(sum(p), ret)


print(ret)
