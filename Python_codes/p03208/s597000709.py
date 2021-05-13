# coding: utf-8

# https://atcoder.jp/contests/abc115


def main():
    N, K = map(int, input().split())
    h = [None] * N
    for i in range(N):
        h[i] = int(input())

    h = sorted(h)

    diff = 10**10
    for i in range(N-K+1):
        newdiff = h[i+K-1]-h[i]
        if newdiff < diff:
            diff = newdiff

    return diff


print(main())
