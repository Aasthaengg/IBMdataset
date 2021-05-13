N, M = map(int, input().split())
G = [[] for _ in range(N)]
res = [10 ** 12] * M
for i in range(M):
    p, y = map(int, input().split())
    G[p - 1].append((y, i))

G = list(map(sorted, G))
for p in range(N):
    for m, (y, i) in enumerate(G[p], 1):
        res[i] += (p + 1) * 10 ** 6 + m

for r in res:
    print(str(r)[1:])
