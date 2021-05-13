MOD = 998244353


def main():
    # 配るdp + imos法
    N, K = (int(i) for i in input().split())
    LR = [[int(i) for i in input().split()] for j in range(K)]

    dp = [0] * (N+2)
    dp[1] = 1
    dp[2] = -1
    for i in range(1, N+1):
        for le, ri in LR:
            if i+le <= N:
                dp[i+le] += dp[i]
                dp[i+le] %= MOD
            if i+ri+1 <= N:
                dp[i+ri+1] -= dp[i]
                dp[i+ri+1] %= MOD
        dp[i+1] += dp[i]
        dp[i+1] %= MOD
    print(dp[N])


if __name__ == '__main__':
    main()
