# coding: utf-8

# https://atcoder.jp/contests/abc108
# 14:20-


def main():
    k = int(input())

    return ((k + (k % 2)) // 2) * (k // 2)


print(main())
