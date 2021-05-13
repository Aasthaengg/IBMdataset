# -*- coding: utf-8 -*-
A, B, K = map(int, input().split())

def is_even(num):
    return num % 2 == 0

for i in range(K):
    if is_even(i):
        if not is_even(A):
            A = A -1
        A, B = A/2, A/2 + B
    else:
        if not is_even(B):
            B = B -1
        B, A = B/2, B/2 + A
    
print(int(A), int(B))