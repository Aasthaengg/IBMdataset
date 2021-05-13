# coding: utf-8

# https://atcoder.jp/contests/abc103
# 11:25-


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = sum([a-1 for a in A])

    return ans


print(main())
