# coding: utf-8

# https://atcoder.jp/contests/abc106
# -12:47 done


def main():
    N, M, Q = map(int, input().split())
    L = [None] * M
    R = [None] * M
    p = [None] * Q
    q = [None] * Q

    for i in range(M):
        L[i], R[i] = map(int, input().split())
        L[i] -= 1
        R[i] -= 1

    for i in range(Q):
        p[i], q[i] = map(int, input().split())
        p[i] -= 1
        q[i] -= 1

    dp = [[0]*N for _ in range(N)]
    for i in range(M):
        dp[L[i]][R[i]] += 1

    for i in range(N-2, -1, -1):
        for j in range(1, N):
            dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1] + dp[i][j]

    for i in range(Q):
        print(dp[p[i]][q[i]])


main()
