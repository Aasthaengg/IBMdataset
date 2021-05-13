#! usr/bin/env python
# -*- coding: utf-8 -*-

MAX_C = 2 * 10 ** 5


def main():
    N = int(input())
    C = [int(input()) for i in range(N)]
    MOD = 10 ** 9 + 7

    NC = []
    CNT = [0] * (MAX_C+1)
    dp = [0] * (N+1)
    idx = 0
    while idx < N:
        NC.append(C[idx])
        while idx < N - 1 and C[idx] == C[idx+1]:
            idx += 1
        idx += 1

    dp[0] = 1
    for i in range(len(NC)):
        c = NC[i]
        dp[i] = (dp[i]+CNT[c]) % MOD
        dp[i+1] = (dp[i+1]+dp[i]) % MOD
        CNT[c] = dp[i]

    print(dp[len(NC)]%MOD)


if __name__ == '__main__':
    main()
