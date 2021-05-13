#!/usr/bin/env python3

import sys, math, copy
# import fractions, itertools
# import numpy as np
# import scipy
# sys.setrecursionlimit(1000000)

HUGE = 2147483647
HUGEL = 9223372036854775807
ABC = "abcdefghijklmnopqrstuvwxyz"

def main():
    n = int(input())
    an = [int(input()) for i in range(n)]
    assert len(an) == n
    sublen = [0 for i in range(n + 1)]
    for i in range(n):
        a1 = an[i]
        sublen[a1] = sublen[a1 - 1] + 1
    res = max(sublen)
    print(n - res)

main()
