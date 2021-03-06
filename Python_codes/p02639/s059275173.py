#!/usr/bin/env python3
# Generated by https://github.com/kyuridenamida/atcoder-tools
from typing import *
import itertools
import math
import sys

INF = float('inf')


def solve(x: "List[int]"):
    return x.index(0) + 1


def main():

    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = [int(next(tokens)) for _ in range(5)]  # type: "List[int]"
    print(solve(x))


if __name__ == '__main__':
    main()
