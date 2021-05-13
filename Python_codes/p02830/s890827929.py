#!/usr/bin/env python3
# Generated by https://github.com/kyuridenamida/atcoder-tools
from typing import *
import collections
import functools
import itertools
import math
import sys

INF = float('inf')


def solve(N: int, S: str, T: str):
    return "".join(s+t for s, t in zip(S, T))


def main():

    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    print(f'{solve(N, S, T)}')


if __name__ == '__main__':
    main()