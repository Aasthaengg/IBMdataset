#BFS
from collections import deque
def bfs(G):
    q=deque()
    q.append((k - 1, -1, 0))

    while q:
        #qの先頭を取り出す
        V, P, C = q.popleft()
        for new, cost in G[V]:
            if new == P:continue
            temp = C + cost
            q.append((new, V, temp))
            stand[new] = temp

n = int(input())
route_list = [[] for i in range(n)]  # 辺の移動の際のコスト
for i in range(n - 1):
    s, t, d = map(int, input().split())
    route_list[s - 1].append((t - 1, d))
    route_list[t - 1].append((s - 1, d))
# print(route_list)
q, k = map(int,input().split())


stand = [0] * n
bfs(route_list)
for i in range(q):
    x, y = map(int,input().split())
    temp = stand[x - 1] + stand[y - 1]
    print(temp)