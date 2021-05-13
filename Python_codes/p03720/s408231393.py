N, M = map(int, input().split())
road_counts = {i: 0 for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    road_counts[a] += 1
    road_counts[b] += 1

[print(road_counts[k]) for k in road_counts]
