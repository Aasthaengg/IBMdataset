#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int):
    ret = 0
    if N > 1:
        ret += N * (N - 1) // 2
    if M > 1:
        ret += M * (M - 1) // 2
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()
