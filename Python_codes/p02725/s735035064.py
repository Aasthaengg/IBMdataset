#!/usr/bin/env python3
# Generated by https://github.com/kyuridenamida/atcoder-tools
from typing import *
import collections
import functools
import itertools
import math
import sys

INF = float('inf')


def solve(K: int, N: int, A: "List[int]"):
    return sum(sorted([(i == 0)*K+A[i]-A[i-1] for i in range(N)])[:-1])


def main():

    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(f'{solve(K, N, A)}')


if __name__ == '__main__':
    main()