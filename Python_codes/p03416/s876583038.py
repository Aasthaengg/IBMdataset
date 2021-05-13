#!/usr/bin/env python3

A, B = map(int, input().split())
ret = 0

for index in range(A, B+1):
    s = str(index)
    if s[:2] == s[5:2:-1]: ret += 1

print(ret)

