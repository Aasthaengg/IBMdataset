#!/usr/bin/env python3
# Generated by https://github.com/kyuridenamida/atcoder-tools
from typing import *
import collections
import itertools
import functools
import math
import sys

INF = float('inf')


def solve(K: int):

    @functools.lru_cache(maxsize=K**3)
    def gcd(a: int, b: int) -> int:
        return math.gcd(a, b)

    return sum([gcd(ab, c+1) for ab in [gcd(a+1, b+1) for a in range(K) for b in range(K)] for c in range(K)])


def main():

    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    print(f'{solve(K)}')


if __name__ == '__main__':
    main()
