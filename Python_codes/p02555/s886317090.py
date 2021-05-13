def solve():
    S = int(input())
    MOD = 10**9+7

    dp = [0] * (S+1)
    dp[0] = 1

    for i in range(1,S+1):
        cnt = 0
        for j in range(i-2):
            cnt += dp[j]
        dp[i] = cnt % MOD
    
    print(dp[S])

if __name__ == '__main__':
    solve()