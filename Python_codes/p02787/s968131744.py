H, N = map(int, input().split())
INF = float('inf')
dp = [INF]*(H+1) #モンスターの体力をi減らすために消耗する魔力の最小値
ans = 0
for n in range(N):
    a,b = map(int, input().split())
    for h in range(1, H + 1):
        if a >= h:
            dp[h] = min(dp[h], b)
        else:
            dp[h] = min(dp[h], dp[h-a] + b)

print(dp[H])