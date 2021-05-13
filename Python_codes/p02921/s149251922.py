#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1 << 32


def solve(S: str, T: str):
    print([S[i] == T[i] for i in range(len(S))].count(True))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)


if __name__ == '__main__':
    main()
