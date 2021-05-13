N, T = map(int, input().split())
best = None
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T and (best is None or c < best):
        best = c
print('TLE' if best is None else best)