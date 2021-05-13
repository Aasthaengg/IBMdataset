N, T = map(int, input().split())
table = [[0] * (N + 1) for _ in range(T + 1)]
dish = sorted((tuple(map(int, input().split())) for _ in range(N)), key=lambda t: t[0])
for t in range(T + 1):
    for n in range(N):
        minutes_to_take, deliciousness = dish[n]
        now = table[t][n]
        if t < T:
            table[min(T, t + minutes_to_take)][n + 1] = max(table[min(T, t + minutes_to_take)][n + 1], now + deliciousness)
        if n < N:
            table[t][n + 1] = max(table[t][n + 1], now)
print(table[T][N])