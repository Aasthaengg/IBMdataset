import numpy as np

def main():
    n, s = map(int, input().split())
    a = [int(i) for i in input().split()]
    mod = 998244353
    dp = np.zeros((n + 1, s + 1), dtype=int)
    dp[0][0] = 1
    for i in range(n):
        ai = a[i]
        dp[i + 1] = dp[i] * 2 % mod
        dp[i + 1, ai:] = (dp[i + 1, ai:] + dp[i, :-ai]) % mod
    print(dp[n][s])

if __name__ == '__main__':
    main()