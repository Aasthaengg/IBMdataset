#!/usr/bin/env python3
n = int(input())
if n % 2 > 0:
    print(0)
else:
    n //= 2
    c = 0
    while n > 0:
        c += n // 5
        n //= 5
    print(c)
