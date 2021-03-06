#!/usr/bin/env python3
import sys


def solve(a: int, b: int, x: int):
    if a % x == 0:
        print(int((b - a) // x + 1))
        return
    next = (x - a % x) + a
    if next > b:
        print(0)
        return
    v = (b - next) // x
    print(v + 1)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    solve(a, b, x)

if __name__ == '__main__':
    main()
