#!/usr/bin/env python3

N = int(input())
A = sorted([int(a) for a in input().split()], reverse=True)

ans = 0
for i, a in enumerate(A):
    if i % 2 == 0:
        ans += a
    else:
        ans -= a

print(ans)
