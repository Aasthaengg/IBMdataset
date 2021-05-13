# coding: utf-8
A, B, C, K = map(int, input().split())

if A == B:
    print(0)
    exit()
if abs(A - B) > 10**18:
    print('Unfair')
elif K % 2 == 1:
    print(B - A)
else:
    print(A - B)