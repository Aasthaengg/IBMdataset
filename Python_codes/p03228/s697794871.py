#!/usr/bin/env python3

A, B, K = map(int, input().split())

def operate(x, y):
    if x % 2 == 1:
        x -= 1
    x //= 2
    return (x, y + x)

for k in range(K // 2):
    A, B = operate(A, B)
    B, A = operate(B, A)
if K % 2 == 1:
    A, B = operate(A, B)

print(A, B)
