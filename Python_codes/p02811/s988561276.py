#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(K: int, X: int):
    if 500 * K >= X:
        print(YES)
    else:
        print(NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(K, X)


if __name__ == "__main__":
    main()
