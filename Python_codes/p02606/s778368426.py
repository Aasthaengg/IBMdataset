#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(L: int, R: int, d: int):
    ret = R // d - (L - 1) // d
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    solve(L, R, d)

if __name__ == '__main__':
    main()
