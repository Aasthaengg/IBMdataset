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


def solve(A: int, B: int, C: int):
    return [NO, YES][not A == B == C and (A == B or B == C or C == A)]


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
    print(f'{solve(A, B, C)}')


if __name__ == '__main__':
    main()