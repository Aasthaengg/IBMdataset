#!/usr/bin/env python3
import sys


def solve(N: int, K: int, S: int):
    if S == 10 ** 9:
        print(" ".join([str(S) for _ in range(K)] + ["1" for _ in range(N - K)]))
    else:
        print(" ".join([str(S) for _ in range(K)] + [str(S + 1) for _ in range(N - K)]))
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    solve(N, K, S)

if __name__ == '__main__':
    main()