N,M = map(int,input().split())
c = list(map(int,input().split()))
dp = list(range(N+1))
for i in range(N+1):
    for ci in c:
        if i + ci <= N:
            dp[i+ci] = min(dp[i+ci],dp[i] + 1)
print(dp[N])
#print(dp)
