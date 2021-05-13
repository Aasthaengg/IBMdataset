#!/usr/bin/env python3
import sys
input = sys.stdin.readline

def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


n = int(input())
div = divisors(n)
div2 = divisors(n-1)

ans = 0
for d in div[1:]:
    tmp = n
    while tmp % d == 0:
        tmp //= d
    if tmp % d == 1:
        ans += 1

print(ans + len(div2) - 1)