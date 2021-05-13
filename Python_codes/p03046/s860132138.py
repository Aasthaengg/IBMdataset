#!/usr/bin/env python3
import functools
import operator

def solve(m, k):
    if k >= 2 ** m:
        return [-1]
    if m == 1 and k == 0:
        return [0, 1, 1, 0]
    b = list(range(2 ** m))
    b.remove(k)
    if functools.reduce(operator.xor, b, 0) != k:
        return [-1]
    a = b + [k] + list(reversed(b)) + [k]
    return a

print(*solve(*map(int, input().split())))
