# coding: utf-8

# https://atcoder.jp/contests/abc104
# 16:23-


def main():
    r = int(input())
    if r < 1200:
        return "ABC"
    elif r < 2800:
        return "ARC"
    else:
        return "AGC"


print(main())
