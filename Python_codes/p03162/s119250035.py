N = int(input())

abc = [[0, 0, 0]]
for _ in range(N):
    a, b, c = map(int, input().split())
    abc.append([a, b, c])

dp = [[0 for _ in range(3)] for _ in range(N + 1)]

# 0=A,1=B, 2=C
for i in range(1, N + 1):
    if i == 1:
        dp[i][0] = abc[1][0]
        dp[i][1] = abc[1][1]
        dp[i][2] = abc[1][2]
    else:
        dp[i][0] = max(dp[i - 1][1] + abc[i][0], dp[i - 1][2] + abc[i][0])
        dp[i][1] = max(dp[i - 1][0] + abc[i][1], dp[i - 1][2] + abc[i][1])
        dp[i][2] = max(dp[i - 1][0] + abc[i][2], dp[i - 1][1] + abc[i][2])

print(max(dp[-1]))
