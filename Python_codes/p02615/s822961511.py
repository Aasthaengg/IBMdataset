#!/usr/bin/env python3
import sys
from itertools import chain

# form bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter
# import numpy as np


# 0123
# 123
#  35

# 0123
# 124
#  3


def solve(N: int, A: "List[int]"):
    A = sorted(A, reverse=True)
    if N == 1:
        return
    N -= 1
    if N % 2 == 0:
        return A[0] + 2 * sum(A[1 : N // 2]) + A[N // 2]
    else:
        return A[0] + 2 * sum(A[1 : (N - 1) // 2 + 1])


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # N, A = map(int, line.split())
    N = int(next(tokens))  # type: int
    A = list(map(int, (tokens)))
    answer = solve(N, A)
    print(answer)


if __name__ == "__main__":
    main()
