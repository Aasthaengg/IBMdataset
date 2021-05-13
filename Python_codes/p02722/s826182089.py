# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10 ** 6)

input_line = input()
inputs = input_line.split(' ')
N, = [int(s) for s in inputs]

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

num = len(make_divisors(N-1))-1

divisors = make_divisors(N)[1:]
for d in divisors:
    t = N
    while t%d==0:
        t = t // d
    if t%d==1:
        num += 1

print(num)

