n = int(input())
costs = list(map(int, input().split()))

if n == 2:
    print(abs(costs[-1] - costs[-2]))
else:
    best = [float("inf") for i in range(n)]
    best[n - 1] = 0
    best[n - 2] =  abs(costs[n - 2] - costs[n - 1])

    for i in range(n - 3, -1, -1):
        best[i] = min(abs(costs[i] - costs[i + 1]) + best[i + 1], abs(costs[i] - costs[i + 2]) + best[i + 2]) 

    print(best[0])

