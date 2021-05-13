from heapq import heappush, heappop
from collections import defaultdict

n = int(input())
graph = defaultdict(list)

# グラフにコストを格納
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q, k = map(int, input().split())


# コストの初期化
INF = 1 << 60
dist = [INF] * (n + 1)
dist[k] = 0

#　スタート地点
que = [(0, k)]

# ３からの距離
while que:
    cost, curr = heappop(que)
    if cost > dist[curr]:
        continue
    for after, nc in graph[curr]:
        if cost + nc < dist[after]:
            dist[after] = cost + nc
            heappush(que, (cost + nc, after))
            
print(*([dist[x] + dist[y] for x, y in (map(int, input().split()) for _ in range(q))]), sep="\n")