N = int(input())
P = list(map(float,input().split()))
dp = [[0] * (N+2) for _ in range(N+1)]
dp[0][0] = 1


for omote in range(N+1):
    for i in range(N):
        dp[i+1][omote] += dp[i][omote] * (1 - P[i])
        dp[i+1][omote+1] += dp[i][omote] * P[i] 

ans = 0
for omote in range(N+1):
    ans += dp[N][omote] if omote > N - omote else 0
print(ans)