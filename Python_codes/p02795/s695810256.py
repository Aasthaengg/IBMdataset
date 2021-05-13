#!/usr/bin/env python3
import sys


def solve(H: int, W: int, N: int):
    if N % max(H, W) != 0:
        print(int(N / max(H, W) + 1))
    else:
        print(int(N / max(H, W)))
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(H, W, N)

if __name__ == '__main__':
    main()