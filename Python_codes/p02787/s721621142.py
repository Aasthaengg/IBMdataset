H, N = map(int, input().split())
magics = []
min_cost = (0, 100000)
max_attack = (0, 100000)
for i in range(N):
    attack, cost = map(int, input().split())
    magics.append((attack,cost))
    if cost < min_cost[1]:
        min_cost = (attack, cost)
    if max_attack[0] < attack:
        max_attack = (attack, cost)
    

dp = [0]
dp.extend([min_cost[1]] * min_cost[0])
for i in range(min_cost[0]+1, H + max_attack[0] + 1):
    minc = 100000000000
    for magic in magics:
        cost = magic[1]
        if 0 < i - magic[0]:
            cost += dp[i - magic[0]]
        if cost < minc:
            minc = cost
    dp.append(minc)
print(min(dp[H:]))