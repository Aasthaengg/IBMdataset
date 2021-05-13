#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(K: int):
    N = 50
    div, mod = divmod(K, N)
    ans = [i+div for i in range(N)]
    for i in range(mod):
        ans[i] += N
        for j in range(N):
            if i == j:
                continue
            ans[j] -= 1

    print(N)
    print(*ans, sep=" ")

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)


if __name__ == '__main__':
    main()
