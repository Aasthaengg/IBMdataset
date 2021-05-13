"""解説を見てから解いたコード"""
N, M, P = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c-P))

INF = float('inf')

coin_map = [-INF] * (N+1)
coin_map[1] = 0

for i in range(2*N):
    for a, b, c in edges:
        if coin_map[b] < coin_map[a] + c:
            coin_map[b] = coin_map[a] + c
            if i >= N:
                coin_map[b] = INF

    if i == N - 1:
        ans = coin_map[N]

if ans != coin_map[N]:
    print(-1)
else:
    print(max(0, coin_map[N]))


