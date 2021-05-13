#!/usr/bin/env python3

MOD = 10**9
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

a, b, c = map(int, input().split())
print(a*b//2)
