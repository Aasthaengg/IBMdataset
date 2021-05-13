#!/usr/bin/env python3

import sys, math, copy
# import fractions, itertools
# import numpy as np
# import scipy

HUGE = 2147483647
HUGEL = 9223372036854775807
ABC = "abcdefghijklmnopqrstuvwxyz"

def main():
    a = input()
    n = len(a)
    di = {c: 0 for c in ABC}
    for c in a:
        di[c] += 1
    invdi = {c: n - di[c] for c in ABC}
    res = 0
    for c in ABC:
        res += di[c] * invdi[c]
    assert res % 2 == 0
    res //= 2
    res += 1
    print(res)


main()
