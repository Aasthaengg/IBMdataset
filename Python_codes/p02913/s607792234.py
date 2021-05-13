def resolve():
    N = int(input())
    S = input()
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in reversed(range(N)):
        for j in reversed(range(N)):
            if S[i] == S[j]:
                dp[i][j] = dp[i+1][j+1] + 1
    
    ans = 0
    for i in range(N):
        for j in range(i, N):
            ans = max(min(dp[i][j], j-i), ans)
    print(ans)


if __name__ == "__main__":
    resolve()