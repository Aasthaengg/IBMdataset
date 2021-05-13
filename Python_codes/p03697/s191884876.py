#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(A: int, B: int):
    ret = A + B
    if A + B >= 10:
        ret = "error"
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
