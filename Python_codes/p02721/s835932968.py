# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10 ** 6)

input_line = input()
inputs = input_line.split(' ')
N, K, C = [int(s) for s in inputs]
input_line = input()
s = list(input_line)

L = []
i = 1
k = 0
while i<=N:
    if s[i-1]=='o':
        L.append(i)
        i += (C+1)
        k += 1
        if k==K:
            break
    else:
        i += 1

R = []
i = N
k = 0
while i>0:
    if s[i-1]=='o':
        R.append(i)
        i -= (C+1)
        k += 1
        if k==K:
            break
    else:
        i -= 1
R = R[::-1]

for i in range(K):
    if L[i]==R[i]:
        print(L[i])
