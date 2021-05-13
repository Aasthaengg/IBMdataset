s = str(input())

n = len(s)

INF = 10**18
dp =[[-INF]*3 for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(3):
        if dp[i][j] == -INF:
            continue
        for k in range(1, 3):
            if j == k:
                if k == 1:
                    if s[i-1] == s[i]:
                        continue
                else:
                    if s[i-2] == s[i] and s[i-1] == s[i]:
                        continue
            if i+k <= n:
                dp[i+k][k] = max(dp[i+k][k], dp[i][j]+1)
print(max(dp[n]))
