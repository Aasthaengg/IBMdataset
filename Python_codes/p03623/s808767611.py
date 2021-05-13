#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(x: int, a: int, b: int):
    if abs(a-x) < abs(b-x):
        print("A")
    else:
        print("B")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(x, a, b)


if __name__ == '__main__':
    main()
