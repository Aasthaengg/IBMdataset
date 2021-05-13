
from collections import deque

# BFSで、B/Wそれぞれのスタート地点から拡張点への距離を取得
def bfs(s, distance):
    visited = [False] * N
    q = [(s, 1)]
    visited[s] = True

    while q:
        u, dist = q.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = dist
                q.append((v, dist+1))

#    print(distance)


N = int(input())
graph = [deque() for i in range(N)]
distance = [[0] * N for i in range(2)]

for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

#print(graph)

bfs(0, distance[0])
bfs(N-1, distance[1])

# 各頂点について、より近いほうが塗れたことに
b = w = 0
for i in range(1, N-1):
    if distance[0][i] <= distance[1][i]:
        b += 1
    else:
        w += 1
if b <= w:
    print('Snuke')
else:
    print('Fennec')
