#!/usr/bin/env python3
import sys
from itertools import chain
# import numpy as np
# from itertools import combinations as comb
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter


def solve(X: int):
    m = 100
    for y in range(1, 3761):
        m += m // 100
        if m >= X:
            return y
    return 3761


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # X = map(int, input().split())
    # X = input().strip()
    X = int(next(tokens))  # type: int
    answer = solve(X)
    print(answer)

if __name__ == '__main__':
    main()
