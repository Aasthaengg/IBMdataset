# -*- coding: utf-8 -*-
"""
D - Prediction and Restriction
https://atcoder.jp/contests/abc149/tasks/abc149_d

"""
import sys


def solve(N, K, R, S, P, T):
    d = {'r': P, 's': R, 'p': S}
    lost = set()
    ans = 0
    for i, ch in enumerate(T):
        if i < K:
            ans += d[ch]
        else:
            if T[i-K] != ch or i-K in lost:
                ans += d[ch]
            else:
                lost.add(i)
    return ans


def main(args):
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = solve(N, K, R, S, P, T)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
