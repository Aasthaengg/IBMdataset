#!/usr/bin/env python3
# N = int(input())
# S = input()
A, B, T= map(int, input().split())
# A = list(map(int, input().split()))
i = 0
while (i + 1) * A <= T + 0.5:
    i += 1
print(B * i)