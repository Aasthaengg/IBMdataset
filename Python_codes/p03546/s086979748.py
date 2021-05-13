"""ABC079D Wall 別解
ワーシャルフロイドでやった場合
"""

H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]

counter = {i: 0 for i in range(-1, 10)}
for i in range(H):
    tmp = list(map(int, input().split()))
    for j in range(W):
        counter[tmp[j]] += 1

dp = c.copy()
for k in range(10):
    for i in range(10):
        for j in range(10):
            dp[i][j] = min(
                dp[i][j],
                dp[i][k] + dp[k][j]
            )

ans = sum([counter[i]*dp[i][1] for i in range(10)])
print(ans)