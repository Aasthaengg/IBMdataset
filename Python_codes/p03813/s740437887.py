#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(x: int):
    if x < 1200:
        print("ABC")
    else:
        print("ARC")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    solve(x)


if __name__ == '__main__':
    main()
