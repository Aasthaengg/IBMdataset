#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(x: int):
    ret = 'ARC'
    if x < 1200:
        ret = 'ABC'
    print(ret)
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
