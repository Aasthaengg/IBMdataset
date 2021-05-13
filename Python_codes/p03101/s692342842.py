# coding: utf-8

# https://atcoder.jp/contests/abc121
# 8:50-


def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())

    return H * W - (h * W + w * (H-h))


print(main())
