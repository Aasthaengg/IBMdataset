#!/usr/bin/env python3
n, m, k = map(int, input().split())
for i in range(n + 1):
    a = k - i * m
    b = n - 2 * i
    if b != 0 and a % b == 0 and 0 <= a // b <= m:
        print("Yes")
        exit()
print("No")
