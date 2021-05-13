n = int(input())
event = []
for _ in range(n):
    event.append(list(map(int,input().split())))

dp = [[0] * 3 for i in range(n)]
dp[0] = event[0]

for i in range(1,n):
    for j in range(3):
        dp[i][j] = max([event[i][j] + dp[i-1][k] for k in range(3) if k != j])

print(max(dp[-1]))