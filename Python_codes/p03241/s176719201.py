#!/usr/bin/env python3


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

N, M = map(int, input().split())

if M%N == 0:
    print(M//N)
else:
    D = sorted(make_divisors(M))[::-1]
    for d in D:
        if M//d >= N:
            print(d)
            break

