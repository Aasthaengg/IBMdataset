#!/usr/bin/env python3

import sys, math, copy
# import fractions, itertools
# import numpy as np
# import scipy

HUGE = 2147483647
HUGEL = 9223372036854775807
ABC = "abcdefghijklmnopqrstuvwxyz"

def get_max_min_mod(a, minp, maxp):
    if minp % a == 0:
        minp_new = (minp // a) * a
    else:
        minp_new = (minp // a + 1) * a
    maxp_new = (maxp // a) * a
    return minp_new, maxp_new

def main():
    k = int(input())
    ak = list(map(int, reversed(input().split())))
    assert len(ak) == k
    minp = maxp = 2
    for j in range(k):
        minp, maxp = get_max_min_mod(ak[j], minp, maxp)
        if minp > maxp:
            print(-1)
            sys.exit(0)
        maxp += ak[j] - 1
    print(minp, maxp)

main()
