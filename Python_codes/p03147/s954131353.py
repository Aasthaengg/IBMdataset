# coding: utf-8

# https://atcoder.jp/contests/abc116


def main():
    N = int(input())
    h = list(map(int, input().split()))

    H = max(h)

    mat = [None] * H
    for i in range(H):
        mat[i] = "".join(["1" if i < h[j] else "0" for j in range(N)])

    ans = 0
    for i in range(H):
        ans += sum([1 if len(s) > 0 else 0 for s in mat[i].split("0")])

    return ans


print(main())
