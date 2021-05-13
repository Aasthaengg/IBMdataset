# coding: utf-8

# https://atcoder.jp/contests/abc118
# 7:55-


def main():
    a, b = map(int, input().split())
    if b % a == 0:
        return a + b
    else:
        return b - a


print(main())
