# coding: utf-8

# https://atcoder.jp/contests/abc090/tasks/arc091_b
# 15:26-


def main():
    N, K = map(int, input().split())

    ans = 0
    for b in range(K+1, N+1):
        if (N+1) % b == 0:
            ans += (N//b+1) * (b-K)
        else:
            ans += N // b * (b-K)
            if N % b >= K:
                ans += N % b - K + 1
        if K == 0:
            ans -= 1

    return ans


print(main())
