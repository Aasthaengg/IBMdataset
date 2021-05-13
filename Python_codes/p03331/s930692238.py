#!/usr/bin/env python3
n = int(input())

ans = 999999

for i in range(1, n):
    a = [int(c) for c in str(i)]
    b = [int(c) for c in str(n - i)]

    k = sum(a) + sum(b)

    if k < ans:
        ans = k

print(ans)