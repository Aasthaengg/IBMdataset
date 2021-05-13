# coding: utf-8

# https://atcoder.jp/contests/abc098/tasks/abc098_a


def main():
    a, b = map(int, input().split())
    return max(a+b, a-b, a*b)


print(main())
