#!/usr/bin/env python3
import sys
from itertools import chain


def solve(K: int, A: int, B: int):
    n = (A + K - 1) // K
    l = n * K
    if l <= B:
        return "OK"
    return "NG"


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    K = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    answer = solve(K, A, B)
    print(answer)


if __name__ == "__main__":
    main()
