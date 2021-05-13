import sys

MOD = 998244353

def main():
    N, S = map(int, input().split())
    X = [int(x) for x in sys.stdin.readline().split()]

    # dp = np.zeros((N+1)*(S+1), dtype=np.int).reshape((N+1),(S+1))
    dp = [[0 for _ in range(S+1)] for _ in range(N+1)]

    dp[0][0] = 1

    for i in range(N):
        xi = X[i]
        # xi を U に加えない場合
        for j in range(S+1):
            dp[i+1][j] += dp[i][j]*2  # T に加える／加えない
            dp[i+1][j] %= MOD
            # xi を U に加える場合
            if j+xi > S: continue
            dp[i+1][j+xi] += dp[i][j]
            dp[i+1][j+xi] %= MOD

    print(dp[N][S] % MOD)

main()