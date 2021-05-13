#!/usr/bin/env python3

A = int(input())
B = int(input())
C = int(input())
D = int(input())

ans = 0

if A > B:
    ans += B
else:
    ans += A

if C > D:
    ans += D
else:
    ans += C

print(ans)