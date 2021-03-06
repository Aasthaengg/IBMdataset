#!/usr/bin/env python3
# Generated by https://github.com/kyuridenamida/atcoder-tools
from typing import *
import collections
import functools
import itertools
import math
import sys

INF = float('inf')


def solve(N: int, A: "List[int]"):
    return ['DENIED', 'APPROVED'][all(a % 2 or a % 3 == 0 or a % 5 == 0 for a in A)]


def main():

    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(f'{solve(N, A)}')


if __name__ == '__main__':
    main()
