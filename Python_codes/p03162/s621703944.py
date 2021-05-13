n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n + 1)]
ans = 0
for d in range(1, n + 1):
    abc = list(map(int, input().split()))
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            dp[d][j] = max(dp[d][j], dp[d - 1][i] + abc[j])
            ans = max(ans, dp[d][j])
print(ans)