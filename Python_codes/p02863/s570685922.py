N, T = list(map(int,input().split()))
AB = [(0,0) for _ in range(N)]

for i in range(N):
    AB[i] = tuple(map(int,input().split()))

AB.sort()

dp = [[0]*(T+1) for _ in range(N+1)]

for t in range(T+1):
    dp[0][t] = 0

for i in range(N):
    for t in range(T+1):
        if t >= AB[i][0]:
            dp[i+1][t] = max(dp[i][t - AB[i][0]] + AB[i][1], dp[i][t])
        else:
            dp[i+1][t] = dp[i][t]

b_max = 0
for i in range(N):
    b_max = max(b_max, dp[i][T-1] + AB[i][1])

print(b_max)