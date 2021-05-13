N, M = map(int, input().split())
A = map(int, input().split())
ok = [0] * 10
for a in A: ok[a] = 1

dp = [-1] * (N + 1)
dp[0] = 0
cost = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for i in range(N):
    for num in range(1, 10):
        c = cost[num]
        if ok[num] == 0 or i + c > N: continue
        dp[i+c] = max(dp[i+c], dp[i] * 10 + num)

ans = dp[N]
print(ans)
