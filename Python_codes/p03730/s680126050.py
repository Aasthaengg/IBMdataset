#!/usr/bin/env python3
A, B, C = map(int, input().split())

n = 0
for i in range(10**4):
    n += A
    if n % B == C:
        print('YES')
        exit()
print('NO')
