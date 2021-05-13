n, ma, mb = map(int, input().split())

INF = 10**10
dp = [[[INF for _ in range(400+5)] for _ in range(400+5)] for _ in range(n+5)]

dp[0][0][0] = 0

for i in range(n):
    a, b, c = map(int, input().split())
    for ta in range(400+5-a):
        for tb in range(400+5-b):
            dp[i+1][ta][tb] = min(dp[i+1][ta][tb], dp[i][ta][tb])
            dp[i+1][ta+a][tb+b] = min(dp[i+1][ta+a][tb+b], dp[i][ta][tb]+c)

ans = INF
for i in range(1, n+1):
    t = 1
    while max(ma, mb)*t <= 400:
        ans = min(ans, dp[i][ma*t][mb*t])
        t += 1

if ans == INF:
    print(-1)
else:
    print(ans)