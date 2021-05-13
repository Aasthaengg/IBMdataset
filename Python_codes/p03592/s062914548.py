#!/usr/bin/env python3

n, m, k = [int(x) for x in input().split()]
for i in range(0, m + 1):
    for j in range(0, n + 1):
        c = i * (n - j) + j * (m - i)
        if c == k:
            print("Yes")
            exit()
print("No")
