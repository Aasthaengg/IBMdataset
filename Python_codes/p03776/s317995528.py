#!/usr/bin/env python3
import sys
from statistics import mean
from bisect import bisect_left
INF = float("inf")


def cmb(n, r):
    if r < 0 or n < r:
        return 0
    r = min(r, n-r)
    if r == 0:
        return 1
    if r == 1:
        return n

    numer = [n - r + k + 1 for k in range(r)]
    denom = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denom[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numer[k - offset] /= pivot
                denom[k] /= pivot

    result = 1
    for k in range(r):
        if numer[k] > 1:
            result *= int(numer[k])

    return result


def solve(N: int, A: int, B: int, v: "List[int]"):
    v.sort()
    ave = mean(v[N-A:])
    ma = v[-1]
    print(ave)

    num = v.count(v[N-A])
    hamidashi = v[:N-A].count(v[N-A])
    if ma == ave and hamidashi > 0:
        # すべて同じ価値の場合
        # A個に拘らなくて良い。
        tot = 0
        for i in range(A, B+1):
            # print(num, hamidashi+i)
            tot += cmb(num, i)
        print(tot)
    else:
        print(cmb(num, hamidashi))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    v = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, v)


if __name__ == '__main__':
    main()
