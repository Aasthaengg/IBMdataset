n, k = (map(int, input().split()))
h = list(map(int, input().split()))

dp = [0, abs(h[0] - h[1])]

for i in range(2, n):
    cost = []
    jump_range = min(i, k) + 1
    for n_jump in range(1, jump_range):
        jump_cost = dp[i - n_jump] + abs(h[i] - h[i - n_jump])
        cost.append(jump_cost)
    dp.append(min(cost))
    cost.clear()

print(dp[-1])
