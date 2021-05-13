#!/usr/bin/env python3
x = int(input())
ans = 1

n = 2

while x >= 2**n:
    c = 1
    while x >= c**n:
        ans = max(ans, c**n)
        c += 1
    n += 1
print(ans)
