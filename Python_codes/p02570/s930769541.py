#!/usr/bin/env python3
# Generated by https://github.com/kyuridenamida/atcoder-tools
from typing import *
import collections
import functools as fts
import itertools as its
import math
import sys

INF = float('inf')
YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(D: int, T: int, S: int):
    return [NO, YES][D/S <= T]


def main():

    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    print(f'{solve(D, T, S)}')


if __name__ == '__main__':
    main()
