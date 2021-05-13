k,t = map(int,input().split())
a = list(map(int,input().split()))

dp = [[False] * (k//2+1) for _ in range(t+1)]

dp[0][0] = True

for i in range(t):
    for j in range(k//2+1):
        if dp[i][j]:
            dp[i+1][j] = True
            if j + a[i] < k//2+1:
                dp[i+1][j + a[i]] = True

cnt = 0
for i,e in enumerate(dp[-1]):
    if e:
        cnt = i

ans = k - (2 * cnt + 1)

print(max(ans, 0))
