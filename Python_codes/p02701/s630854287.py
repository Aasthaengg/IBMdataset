#!/usr/bin/env python3
import sys
from itertools import chain


def solve(N: int, S: "List[str]"):
    return len(set(S))


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    answer = solve(N, S)
    print(answer)


if __name__ == "__main__":
    main()
