N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

cost = [0,2,5,5,4,5,6,3,7,6]

dp = [-1 for _ in range(N + 1)] #dp[i] i本のマッチを使って作れる最大の桁数
dp[0] = 0

for i in range(1, N + 1):
    for a in A:
        if i - cost[a] >= 0:
            dp[i] = max(dp[i], dp[i - cost[a]] + 1)

ans = ''

i = N
for k in range(dp[N]):
    for a in A:
        if i - cost[a] >= 0 and dp[i - cost[a]] != -1 and dp[i - cost[a]] == dp[i] - 1:
            ans += str(a)
            i -= cost[a]
            break

print(ans)