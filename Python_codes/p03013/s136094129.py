N, M = map(int, input().split())
a = []
oks = [1] * (N+1)
for i in range(M):
    a.append(int(input()))
    oks[a[i]] = 0

dp = [0] * (N+1)
dp[0] = 1

for now in range(N):
    for nex in range(now+1, min(N, now+2) + 1):
        if oks[nex] == 1:
            dp[nex] += dp[now]
            dp[nex] %= 10 ** 9 + 7

print(dp[N])