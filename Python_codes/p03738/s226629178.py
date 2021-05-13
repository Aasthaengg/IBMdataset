# -*- coding: utf-8 -*-

A = list(str(input()))
B = list(str(input()))

if len(A) > len(B):
    print('GREATER')
elif len(A) < len(B):
    print('LESS')
elif A == B:
    print('EQUAL')
else:
    for i in range(len(A)):
        if A[i] > B[i]:
            print('GREATER')
            break
        elif A[i] < B[i]:
            print('LESS')
            break