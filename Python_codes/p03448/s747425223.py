#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int):
    ans = 0
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                ans += (a * 500 + b * 100 + c * 50) == X
    return ans


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    print(solve(A, B, C, X))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()