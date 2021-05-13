import sys
MOD = 998244353
def main():
    input = sys.stdin.readline
    N, S = map(int, input().split())
    *A, = map(int, input().split())
    # dp[i][j]=i番目まで見て合計がjになる組み合わせの数
    dp = [[0] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        a = A[i - 1]
        for k in range(S + 1):
            # i番目を使わない
            dp[i][k] = (dp[i][k] + dp[i - 1][k] * 2) % MOD
            # i番目を使う
            if k >= a:
                dp[i][k] = (dp[i][k] + dp[i - 1][k - a]) % MOD
    print(dp[N][S])

if __name__ == '__main__':
    main()
