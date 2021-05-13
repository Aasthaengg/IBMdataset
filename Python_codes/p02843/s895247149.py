
X = int(input())

dp = [False] * (X + 1)
cost = [100, 101, 102, 103, 104, 105]
dp[0] = True
for i in range(X):
    for j in range(6):
        if dp[i] and i + cost[j] <= X:
            dp[i + cost[j]] = True

if dp[-1]:
    print(1)
else:
    print(0)
