from heapq import heappop, heappush

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    graph[a].append(b)

S, T = map(lambda x: int(x)-1, input().split())

ans = -1
visited = set()  # 通常であればvisited = [False]*N
q = [(0, S)]
while q:
    c, v = heappop(q)  # cはカウント, vは頂点の番号
    key = (c % 3, v)
    if key in visited:
        continue
    visited.add(key)  # グラフのノードの番号だけでなく、カウントも記録していく
    if v == T and c % 3 == 0:
        ans = c//3
        break
    c += 1  # u, 0から伸びる辺はv, 1で、u, 1から伸びる辺はv, 2
    d = c % 3  # 三種類の状態を記録したいのでmod3
    for u in graph[v]:
        new_key = (d, u)
        if new_key in visited:
            continue
        heappush(q, (c, u))

print(ans)
