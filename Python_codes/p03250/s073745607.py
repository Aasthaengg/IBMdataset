# coding: utf-8

# https://atcoder.jp/contests/abc110
# 14:05-


def main():
    a, b, c = map(int, input().split())
    abc = sorted([a, b, c], reverse=True)

    return abc[0] * 10 + abc[1] + abc[2]


print(main())
