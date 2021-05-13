N, M, X = [int(a) for a in input().split()]
A = [int(a) for a in input().split()]

cost = [0 for _ in range(N+1)]
for a in A:
    cost[a] = 1

cost_1 = 0
cost_2 = 0
for i in range(N+1):
    if i < X:
        cost_1 += cost[i]
    elif i > X:
        cost_2 += cost[i]

print(min(cost_1,cost_2))