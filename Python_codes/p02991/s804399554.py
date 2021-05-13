from collections import deque

N, M = map(int, input().split())
link = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    link[a-1].append(b-1)
s, t = map(lambda x: int(x)-1, input().split())

INF = 10 ** 10
dist = [[INF] * 3 for _ in range(N)]
dist[s][0] = 0

que = deque([[s, 0]])

while len(que):
    pv, pl = que.popleft()
    for nv in link[pv]:
        nl = (pl + 1) % 3
        if dist[nv][nl] != INF:
            continue
        dist[nv][nl] = dist[pv][pl] + 1
        que.append([nv, nl])

ans = dist[t][0]
if ans == INF:
    ans = -1
else:
    ans //= 3

print(ans)
