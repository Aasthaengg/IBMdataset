#!/usr/bin/env python3
import sys

input = sys.stdin.readline


def I():
    return int(input())


n = I()

ans = 0
for x in range(1, n + 1):
    y = n // x
    ans += x * y * (y + 1) // 2

print(ans)
