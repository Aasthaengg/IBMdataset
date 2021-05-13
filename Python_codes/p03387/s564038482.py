# -*- coding: utf-8 -*-

A,B,C = map(int, input().split())

s = A + B + C
M = max(A,B,C)
if M % 2 == 0 and s % 2 != 0:
    M += 1
elif M % 2 != 0 and s % 2 == 0:
    M += 1

ans = (3 * M - s) / 2
print(int(ans))
