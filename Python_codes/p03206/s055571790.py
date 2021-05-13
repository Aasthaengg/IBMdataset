# coding: utf-8

# https://atcoder.jp/contests/abc115
# 10:10-


def main():
    d = int(input())
    if d == 25:
        return "Christmas"
    elif d == 24:
        return "Christmas Eve"
    elif d == 23:
        return "Christmas Eve Eve"
    else:
        return "Christmas Eve Eve Eve"


print(main())
