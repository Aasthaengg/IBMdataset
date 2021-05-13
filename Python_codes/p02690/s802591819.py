#!/usr/bin/env python3
x = int(input())


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors


for i in make_divisors(x):
    a = 0
    while (a - i) < 0 or a**5 - (a - i)**5 < x:
        a += 1
        if a**5 - (a - i)**5 == x:
            print(a, a - i)
            exit()
