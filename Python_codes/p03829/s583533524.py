num_towns, cost_walk, cost_warp = map(int, input().split())
positions = list(map(int, input().split()))

total_cost = 0
for p1, p2 in zip(positions[:-1], positions[1:]):
    c_walk = (p2 - p1) * cost_walk
    if c_walk < cost_warp:
        total_cost += c_walk
    else:
        total_cost += cost_warp

print(total_cost)
