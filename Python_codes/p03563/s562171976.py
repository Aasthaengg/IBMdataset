#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(R: int, G: int):
    print(G*2-R)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    solve(R, G)


if __name__ == '__main__':
    main()
