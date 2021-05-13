#!/usr/bin/env python3

A,B,C = [int(x) for x in input().split(" ")]

ans = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    ans += 1
    A_new = B / 2 + C / 2
    B_new = A / 2 + C / 2
    C_new = A / 2 + B / 2
    if A == A_new and B == B_new and C == C_new:
        ans = -1
        break
    A = A_new
    B = B_new
    C = C_new

print(ans)
