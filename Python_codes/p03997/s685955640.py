#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(a: int, b: int, h: int):
    print(h*(a+b)//2)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    h = int(next(tokens))  # type: int
    solve(a, b, h)


if __name__ == '__main__':
    main()
