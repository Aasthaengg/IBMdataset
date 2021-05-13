#!/usr/bin/env python3

X = int(input())

ans = 0
for i in range(1, 10**9):
    ans += i
    if ans >= X:
        print(i)
        exit()
