# -*- coding: utf-8 -*-
n,m,l = [int(i)for i in input().split(' ')]
A = []
B = []
C = [[0for _ in range(l)]for _ in range(n)]
for i in range(n):
    A.append([int(a)for a in input().split(' ')])
for i in range(m):
    B.append([int(a)for a in input().split(' ')])

for i in range(n):
    for j in range(l):
        s = 0
        for k in range(m):
            s += A[i][k]*B[k][j]
        C[i][j] = s

for x in range(n):
    print(' '.join([str(a)for a in C[x]]))