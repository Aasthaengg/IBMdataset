#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, K: int):
    print(K*((K-1)**(N-1)))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == '__main__':
    main()
