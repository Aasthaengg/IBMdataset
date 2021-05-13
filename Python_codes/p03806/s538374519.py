n, ma, mb = map(int, input().split())
items = []
for i in range(n):
    item = list(map(int, input().split()))
    items.append(item)

# dp[iまでの薬品を使用して][aの重量][bの重量]を達成する最小の予算
dp = [[[float('inf')]*401 for j in range(401)] for i in range(41)]
dp[0][0][0] = 0

for i in range(n):
    a, b, c = items[i]
    for anow in range(400):
        for bnow in range(400):
            # 使わない
            dp[i+1][anow][bnow] = min(dp[i+1][anow][bnow], dp[i][anow][bnow])
            # 使う
            if 0<=anow+a<401 and 0<=bnow+b<401:
                dp[i+1][anow+a][bnow+b] = min(dp[i+1][anow+a][bnow+b], dp[i][anow][bnow]+c)
                

ans = float('inf')
for a in range(1, 401):
    for b in range(1, 401):
        if ma*b==mb*a:
            ans = min(ans, dp[n][a][b])
if ans == float('inf'):
    print(-1)
else:
    print(ans)