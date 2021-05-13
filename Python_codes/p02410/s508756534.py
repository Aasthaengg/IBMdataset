# -*- coding: utf-8 -*-
A = []
B = []
n,m = [int(i) for i in input().split(' ')]

for i in range(n):
    A.append([int(j) for j in input().split(' ')])
for j in range(m):
    B.append(int(input()))
#print(A)
#print(B)
c =0
for i in range(n):
    for j in range(m):
        c +=A[i][j] * B[j]
    print(c) 
    c =0