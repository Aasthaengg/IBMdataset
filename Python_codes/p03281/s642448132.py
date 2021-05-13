#!/usr/bin/env python3
n = int(input())
c = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n // i + 1):
        c[j * i] += 1
print(sum(c[i] == 8 for i in range(1, n + 1, 2)))
