cost = [int(input()) for _ in range(4)]
print(min(cost[0] + cost[2], cost[0] + cost[3],
          cost[1] + cost[2], cost[1] + cost[3]))