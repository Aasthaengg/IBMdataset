#!/usr/bin/env python3
import sys

MAX = 10 * 18


def solve(A: int, B: int, C: int, K: int):
    ans = A - B
    if K % 2 != 0:
        ans *= -1
    print(ans)

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(A, B, C, K)

if __name__ == '__main__':
    main()