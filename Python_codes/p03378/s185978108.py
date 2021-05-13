n, m, x = map(int, input().split())
a = list(map(int, input().split()))

cost = [0 for _ in range(n + 1)]
for ai in a:
    cost[ai] = 1
print(min(sum(cost[:x]), sum(cost[x:])))
