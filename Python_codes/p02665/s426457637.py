#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    if N == 0:
        if A == [0]:
            print('0')
        elif A == [1]:
            print('1')
        else:
            print('-1')
        return

    if N == 1:
        if A == [0, 1]:
            print('2')
        elif A == [0, 2]:
            print('3')
        else:
            print('-1')
        return

    if A[0] != 0:
        print('-1')
        return

    f = [0 for i in range(N)]

    f[0] = 1
    count = sum(A) - 1

    for d in range(1, N):
        f[d] = 2 * min(f[d - 1], count) - A[d] + min(max(f[d - 1] - count, 0), f[d - 1])
        count -= min(f[d - 1], count)
        if f[d] <= 0:
            print('-1')
            return

    if A[-1] > 2 * f[N-1]:
        print('-1')
        return

    print(sum(f) + sum(A))
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 0 + 1)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
