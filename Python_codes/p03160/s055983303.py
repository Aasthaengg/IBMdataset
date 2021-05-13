n = int(input())
costs = list(map(int, input().split()))

if n == 2:
    print(abs(costs[-1] - costs[-2]))
else:
    best = [abs(costs[n - 2] - costs[n - 1]), 0]

    for i in range(n - 3, -1, -1):
        current = min(abs(costs[i] - costs[i + 1]) + best[0], abs(costs[i] - costs[i + 2]) + best[1])
        best[0], best[1] = current, best[0] 

    print(best[0])

