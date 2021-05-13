# coding: utf-8

# https://atcoder.jp/contests/abc105
# 12:25-


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    S = [None] * (N+1)
    S[0] = 0
    s = 0
    for i in range(N):
        s += A[i]
        S[i+1] = s
    
    R = [s % M for s in S]
    d = {}
    for r in R:
        if r in d:
            d[r] += 1
        else:
            d[r] = 1

    ans = 0
    for n in d.values():
        ans += n * (n-1) // 2

    return ans


print(main())
