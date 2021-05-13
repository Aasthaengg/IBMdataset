# coding: utf-8

# https://atcoder.jp/contests/abc101


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 1
    N -= K
    if N % (K-1) == 0:
        ans += N // (K-1)
    else:
        ans += N // (K-1) + 1
    
    return ans


print(main())
