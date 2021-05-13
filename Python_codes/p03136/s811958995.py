# coding: utf-8

# https://atcoder.jp/contests/abc117


def main():
    N = int(input())
    L = list(map(int, input().split()))

    L = sorted(L, reverse=True)

    if L[0] < sum(L[1:]):
        return "Yes"
    else:
        return "No"


print(main())
