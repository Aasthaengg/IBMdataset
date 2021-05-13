costs = list(map(int, input().split()))

costs.sort()
diff = [(costs[i + 1] - costs[i]) for i in range(len(costs) - 1)]

ans = sum(diff)

print(ans)