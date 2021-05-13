from collections import deque
INF = float("inf")

N, M = map(int, input().split())

# i + 0*N -> (3の倍数)回で移動できるi
# i + 1*N -> (3の倍数+1)回で移動できるi
# i + 2*N -> (3の倍数+2)回で移動できるi

# 有向グラフなので、u -> vのみ （v -> u は通れない）
G = [[] for _ in range(3 * N)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    G[u].append(v + N)
    G[u + N].append(v + 2 * N)
    G[u + 2 * N].append(v)

S, T = map(int, input().split())
S, T = S - 1, T - 1

ans = [INF] * (3 * N)
ans[S] = 0
dq = deque([S])

# BFS
while dq:
    now = dq.popleft()
    for next in G[now]:
        if ans[next] != INF:
            continue
        ans[next] = ans[now] + 1
        dq.append(next)

# 3の倍数回で移動できる、Tへの最短距離 = ans[T + 0*N]
if ans[T] != INF:
    print(ans[T] // 3)
else:
    print(-1)
