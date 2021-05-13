# -*- coding: utf-8 -*-
import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, Q, *A = map(int, read().split())

    B = [0] * N
    for a in A:
        B[a - 1] += 1

    ans = [0] * N
    for i, b in enumerate(B):
        if Q >= K + b:
            ans[i] = 'No'
        else:
            ans[i] = 'Yes'

    print('\n'.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()
