from itertools import permutations


N, M, *ab = map(int, open(0).read().split())
g = [[0] * N for _ in range(N)]
for a, b in zip(*[iter(ab)] * 2):
    g[a - 1][b - 1] = 1
    g[b - 1][a - 1] = 1

ans = 0
for path in permutations(range(1, N)):
    path = [0] + list(path)
    if all(g[v][nv] for v, nv in zip(path, path[1:])):
        ans += 1
print(ans)
