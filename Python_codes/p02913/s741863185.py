def solve():
    N = int(input())
    Ss = input().rstrip()

    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in reversed(range(N)):
        for j in reversed(range(N)):
            if Ss[i] == Ss[j]:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = 0

    ans = 0
    for i in range(N):
        for j in range(N):
            L = j-i if j-i <= dp[i][j] else dp[i][j]
            if L > ans:
                ans = L

    print(ans)


solve()
