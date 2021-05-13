# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split(' ')))

ret = 0
for i in range(1, N):
    if A[i-1] == A[i]:
        A[i] = -1
        ret += 1

print(ret)


