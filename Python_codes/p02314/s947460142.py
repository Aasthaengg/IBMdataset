# -*- coding: utf-8 -*-

import sys
import os
import pprint

#fd = os.open('DPL_1_A.txt', os.O_RDONLY)
#os.dup2(fd, sys.stdin.fileno())

# n: n???????????????
# m: m?¨????????????????
n, m = list(map(int, input().split()))
C = list(map(int, input().split()))
MAX = 50000

# i???????????§????????????????????£???j????????????????°??????°
# T[i][j]
# m * (MAX + 1) ?¬????
T = [[float('inf') for i in range(MAX + 1)] for j in range(m)]

#print(n, '???????????????')
for i in range(0, m):
    T[i][0] = 0
    for j in range(1, n + 1):
        #print('i', i, 'j', j, 'C[i]', C[i], 'T[i,j]', T[i][j])
        if C[i] <= n:
            T[i][j] = min(T[i-1][j], T[i][j - C[i]] + 1)
        else:
            T[i][j] = T[i - 1][j]

print(T[m-1][n])