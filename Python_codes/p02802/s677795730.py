#!/usr/bin/env python3
import sys
from itertools import chain

# import numpy as np
# from itertools import combinations as comb
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter


def solve(N: int, M: int, P: "List[int]", S: "List[str]"):
    ac = [0] * N
    wa = [0] * N
    for p, s in zip(P, S):
        if s == "AC":
            ac[p - 1] = 1
        else:  # WA
            if ac[p - 1] == 0:
                wa[p - 1] += 1
    for i in range(N):
        if ac[i] == 0:
            wa[i] = 0

    return sum(ac), sum(wa)


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = [int()] * (M)  # type: "List[int]"
    S = [str()] * (M)  # type: "List[str]"
    for i in range(M):
        P[i] = int(next(tokens))
        S[i] = next(tokens)
    a1, a2 = solve(N, M, P, S)
    print(a1, a2)


if __name__ == "__main__":
    main()
