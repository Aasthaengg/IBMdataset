import copy

h, w = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(10)]

# ワーシャルフロイド法で更新がなくなるまで更新
while True:
    prev = copy.deepcopy(dp)
    for k in range(10):
        for i in range(10):
            for j in range(10):
                if i == j:
                    continue
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    if prev == dp:
        break
    prev = dp

ans = 0
for i in range(h):
    arr = list(map(int, input().split()))
    ans += sum([dp[x][1] for x in arr if x != -1])

print(ans)