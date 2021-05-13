n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
INF = 10**9 + 1
dp = [[INF]*n for _ in range(n)]

# コスト登録
for i, line in enumerate(A):
    for j, a in enumerate(line):
        dp[i][j] = a

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        d = dp[i][j]
        if d < A[i][j]:
            ans = -1
            break
        else:
            for k in range(n):
                if k == i or k == j:
                    continue
                if dp[i][k] + dp[k][j] == d:
                    break
            else:
                ans += d
    if ans == -1:
        break
print(ans)
