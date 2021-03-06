#!/usr/bin/env python3
# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
import sys


def solve(N: int, M: int):
    f = M % 2 == 0
    for i in range(M//2):
        print(f'{i+1} {M-i+f}')
    for i in range((M+1)//2):
        print(f'{M+i+1+f} {2*M-i+1}')


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
