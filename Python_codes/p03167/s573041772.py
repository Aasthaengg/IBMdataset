h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(input())

dp = [0]*(w+1)
dp[1] = 1
for i in grid:
    newdp = dp[:]
    for j, k in enumerate(i):
        newdp[j+1] = dp[j+1] + newdp[j] if k=='.' else 0
    dp = newdp
print(dp[-1]%(10**9+7))