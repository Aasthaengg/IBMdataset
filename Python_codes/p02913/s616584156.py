N = int(input())
S = input()

res = 0
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in reversed(range(N)):
    for j in reversed(range(i + 1, N)):
        if S[i] == S[j]:
            dp[i][j] = max(dp[i][j], dp[i + 1][j + 1] + 1)
        res = max(res, min(dp[i][j], j - i))
        
print(res)
