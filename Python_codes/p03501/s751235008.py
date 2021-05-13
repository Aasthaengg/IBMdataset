# -*- coding: utf-8 -*-S
N,A,B = [int(i) for i in input().split()]

if A * N <= B:
    print(A * N)
elif A * N > B:
    print(B)
