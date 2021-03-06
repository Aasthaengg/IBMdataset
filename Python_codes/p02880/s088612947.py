#!/usr/bin/env python3
# Generated by https://github.com/kyuridenamida/atcoder-tools
from typing import *
import collections
import functools
import itertools
import math
import sys

INF = float('inf')
YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int):
    return [NO, YES][N in [i * j for i in range(1, 10) for j in range(i, 10)]]


def main():

    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    print(f'{solve(N)}')


if __name__ == '__main__':
    main()
