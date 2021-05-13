#!/usr/bin/env python3
import sys
from itertools import chain


def solve(N: int, S: str, T: str):
    answer = "".join([st[0] + st[1] for st in zip(S, T)])
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    answer = solve(N, S, T)
    print(answer)


if __name__ == "__main__":
    main()
