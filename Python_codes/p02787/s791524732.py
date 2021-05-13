H, N = map(int, input().split())
magic = [list(map(int, input().split())) for i in range(N)]

# dp[damage] := モンスターに damage を与えるために必要な最小コスト

# damage = 0,1,2,...,H
dp = [10**9] * (H + 1)
dp[0] = 0
for h in range(H):
    for damage, cost in magic:
        next_index = min(h + damage, H)
        dp[next_index] = min(dp[next_index], dp[h] + cost)

# print(dp)
print(dp[-1])
