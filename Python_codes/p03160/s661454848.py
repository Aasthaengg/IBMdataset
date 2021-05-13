def min_cost():
    # Translation of Errichto's solution
    len_costs = input()
    costs = input().split(' ')
    costs = list(map(int, costs))
    dp = [float('inf') for i in range(len(costs))]
    dp[0] = 0
    for i in range(len(costs)):
        for j in [i + 1, i + 2]:
            if j < len(costs):
                dp[j] = min(dp[j], dp[i] + abs(costs[i] - costs[j]))
    print(dp[-1])

min_cost()
# min_cost([10, 30, 40, 20])
# min_cost([10, 10])
# min_cost([30, 10, 60, 10, 60, 50])
