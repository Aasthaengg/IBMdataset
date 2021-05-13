# -*- coding: utf-8 -*-
"""
C - 二人のアルピニスト / Two Alpinists
https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_c

"""
import sys


def solve(N, T, A):
    mountains_t = dict()
    peak_t = T[0]
    mountains_t[1] = (peak_t, peak_t)
    for i, t in enumerate(T[1:], start=2):
        if t > peak_t:
            peak_t = t
            mountains_t[i] = (peak_t, peak_t)
        else:
            if t < peak_t:
                return 0
            mountains_t[i] = (1, peak_t)

    mountains_a = dict()
    peak_a = A[-1]
    mountains_a[N] = (peak_a, peak_a)
    for j, a in zip(range(N-1, 0, -1), reversed(A[:-1])):
        if a > peak_a:
            peak_a = a
            mountains_a[j] = (peak_a, peak_a)
        else:
            if a < peak_a:
                return 0
            mountains_a[j] = (1, peak_a)

    MOD = 10**9 + 7
    ans = 1
    for i in range(1, N+1):
        lt, ht = mountains_t[i]
        la, ha = mountains_a[i]
        if lt == ht or la == ha:
            if lt == ht and la == ha:
                if lt != la:
                    return 0
            elif lt == ht:
                if not la <= lt <= ha:
                    return 0
            else:
                if not lt <= la <= ht:
                    return 0
        else:
            high = min(ht, ha)
            ans = ans * high% MOD
    return ans


def main(args):
    N = int(input())
    T = [int(t) for t in input().split()]
    A = [int(a) for a in input().split()]
    ans = solve(N, T, A)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
