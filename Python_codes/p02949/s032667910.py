INF = 10 ** 10
N, M, P = map(int, input().split())
edge = []
for i in range(M):
    a, b, c = map(int, input().split())
    edge.append((a - 1, b - 1, c - P))

d = [-INF] * N
d[0] = 0

for i in range(N - 1):
    for a, b, c in edge:
        if d[a] != -INF and d[b] < d[a] + c:
            d[b] = d[a] + c

ans = d[-1]

for i in range(N - 1):
    for a, b, c in edge:
        if d[a] != -INF and d[b] < d[a] + c:
            d[b] = INF

if ans != d[-1]:
    print(-1)
else:
    print(max(0, d[N - 1]))
