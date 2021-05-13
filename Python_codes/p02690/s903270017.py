#!/usr/bin/env python3
import sys
from itertools import chain

# import numpy as np
# from itertools import combinations as comb
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter
import math


def get_factors(X):
    """Xの約数を求める"""
    factors = []
    for i in range(1, math.ceil(X ** 0.5) + 1):
        if X % i == 0:
            factors.append(i)
            factors.append(X // i)
    factors.append(X)
    return sorted(factors)


def solve(X: int):
    factors = get_factors(X)

    # B < 0 の時
    a_max = math.floor(X ** (1 / 5))
    # A - B は X の約数
    for amb in factors:
        for a in range(1, a_max + 1):
            b = a - amb
            if a ** 5 - b ** 5 == X:
                return str(a) + ' ' + str(b)

    # B >= 0 の時
    a_min = math.ceil(X ** (1 / 5))
    a_max = math.floor(X ** (1 / 4))
    # A - B は X の約数
    for amb in factors:
        for a in range(a_min, a_max + 1):
            b = a - amb
            if a ** 5 - b ** 5 == X:
                return str(a) + ' ' + str(b)

    return (0, 0)


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # X = map(int, line.split())
    X = int(next(tokens))  # type: int
    answer = solve(X)
    print(answer)


if __name__ == "__main__":
    main()
