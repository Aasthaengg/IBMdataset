import sys
input = sys.stdin.readline

def main():
    N = int(input())
    dp = [[0] * 4 if i != 3 else [1] * 4 for i in range(N+3)]
    MOD = int(1e9) + 7
    for i in range(4, N+3):
        sum_pre = sum(dp[i-1]) % MOD
        # A
        dp[i][0] = sum_pre
        # C
        dp[i][1] = (sum_pre - dp[i-2][0] - dp[i-2][2] - dp[i-3][0] * 3) % MOD
        # G
        dp[i][2] = (sum_pre - dp[i-2][0] + dp[i-3][2]) % MOD
        # T
        dp[i][3] = sum_pre
    print(sum(dp[-1]) % MOD)

if __name__ == "__main__":
    main()