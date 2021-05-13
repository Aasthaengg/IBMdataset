#!/usr/bin/env python3
# Generated by https://github.com/kyuridenamida/atcoder-tools
from typing import *
import collections
import itertools
import math
import sys

INF = float('inf')
YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, A: "List[int]"):
    t = sum(A)/4/M
    return [YES, NO][len([a for a in A if a >= t]) < M]


def main():

    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(f'{solve(N, M, A)}')


if __name__ == '__main__':
    main()