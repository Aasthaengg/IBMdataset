N,K = map(int,input().split())
a = list(map(int,input().split()))

d = 60
dp = [[-1]*N for _ in range(d+1)]
for i in range(N):
    dp[0][i] = a[i]-1

for i in range(d):
    for j in range(N):
        dp[i+1][j] = dp[i][dp[i][j]]

ans = 0

for i in range(d):
    if K & (1<<i):
        ans = dp[i][ans]

print(ans+1)


