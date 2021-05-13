n = int(input())

abc = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for i in range(n + 1)]
dp[0] = [0, 0, 0]

for i in range(n): # i represents i_th day
    for j in range(3): # j represents j_th activity chosen on the i_th day
        for k in range(3): # k represents k_th activity to be chosen on the day after
            if k != j:
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + abc[i][k])
print(max(dp[n]))