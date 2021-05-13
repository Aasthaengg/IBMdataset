#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(a: int, b: int, h: int):
    ret = (b + a) * h / 2
    print(int(ret))
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
