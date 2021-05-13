#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(A: int, B: int, X: int):
    return YES if A <= X < (A+B) else NO


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    print(solve(A, B, X))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()