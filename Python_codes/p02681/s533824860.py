#!/usr/bin/env python3
import sys
from itertools import chain

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str, T: str):
    return YES if T[: len(S)] == S else NO


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    answer = solve(S, T)
    print(answer)


if __name__ == "__main__":
    main()
