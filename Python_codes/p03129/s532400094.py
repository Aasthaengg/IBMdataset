#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(N: int, K: int):
    if N >= 2 * (K - 1) + 1:
        ret = YES
    else:
        ret = NO
    print(ret)
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
