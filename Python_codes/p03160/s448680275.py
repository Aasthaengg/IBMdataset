N = int(input())
h = [int(x) for x in input().split()]

cost = [0] * N
cost[0] = 0
cost[1] = abs(h[1] - h[0])
for i in range(2, N):
    cost[i] = min(cost[i - 1] + abs(h[i] - h[i - 1]), cost[i - 2] + abs(h[i] - h[i - 2]))

print(cost[N - 1])