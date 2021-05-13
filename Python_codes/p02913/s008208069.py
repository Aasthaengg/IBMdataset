def main():
    N = int(input())
    S = input()

    ans = 0
    dp = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            if S[i] == S[j]:
                dp[i][j] = dp[i+1][j+1] + 1
                tmp = min(dp[i][j], j-i)
                ans = max(ans, tmp)
    print(ans)

if __name__ == "__main__":
    main()
