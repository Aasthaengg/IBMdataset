#!/usr/bin/env python3
# Generated by https://github.com/kyuridenamida/atcoder-tools
from typing import *
import itertools
import math
import sys

INF = float('inf')


def solve(A: int, B: int, C: int, K: int):
    return min(K, A) - max(K-A-B, 0)


def main():

    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    print(solve(A, B, C, K))


if __name__ == '__main__':
    main()
