#!/usr/bin/env python3
def main():
    import numpy as np

    N, K = map(int, input().split())
    section = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353

    dp = np.zeros(N + 1, dtype=np.int64)
    dp[1] = 1
    cumsum = np.zeros(N + 1, dtype=np.int64)
    cumsum[1] = 1
    for i in range(2, N + 1):
        for left_section, right_section in section:
            left = max(i - right_section - 1, 0)
            right = i - left_section
            if right < 0:
                continue
            dp[i] += cumsum[right] - cumsum[left]
        cumsum[i] = cumsum[i - 1] + dp[i]
        dp[i] %= MOD
        cumsum[i] %= MOD
    print(dp[N] % MOD)
    # print(dp)
    # print(cumsum)


if __name__ == '__main__':
    main()
