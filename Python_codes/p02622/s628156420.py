#!/usr/bin/env python3
import sys
from itertools import chain


def solve(S: str, T: str):
    answer = sum([s != t for s, t in zip(S, T)])
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    answer = solve(S, T)
    print(answer)


if __name__ == "__main__":
    main()
