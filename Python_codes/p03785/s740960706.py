N, C, K = map(int, input().split())
t_sorted = [int(input()) for _ in range(N)]
t_sorted.sort()

car = 0
passenger = 0
target_t, limit = 0, 0
for i, t in enumerate(t_sorted):
    if target_t == 0:
        target_t = t
        limit = t + K
    passenger += 1
    if passenger == C:
        car += 1
        passenger = 0
        target_t = 0
        continue
    if i != N - 1:
        if t_sorted[i + 1] > limit:
            car += 1
            passenger = 0
            target_t = 0
            continue
if passenger > 0:
    car += 1

print(car)
