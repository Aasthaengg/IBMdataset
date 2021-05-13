cost = [int(s) for s in input().split()]
min_cost = 0
for i in range(3):
    total_cost = cost[i] + cost[(i + 1) % 3] 
    if (min_cost == 0) | (total_cost < min_cost):
        min_cost = total_cost
print(min_cost)