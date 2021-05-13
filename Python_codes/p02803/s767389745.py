# 幅優先探索
from collections import deque
H, W = map(int, input().split())
dif = [(-1, 0), (1, 0), (0, 1), (0, -1)]
Map = [list(input()) for i in range(H)]
visited = [[False for i in range(W)] for j in range(H)]
deq = deque()


def bfs(node):
    nx, ny = node
    deq.append(node)

    visited[nx][ny] = True
    distance = [[float("inf") for i in range(W)] for j in range(H)]
    distance[nx][ny] = 0
    while deq:
        x, y = deq.popleft()
        for dx, dy in dif:
            if 0 <= x+dx < H and 0 <= y+dy < W and Map[x+dx][y+dy] == "." and visited[x+dx][y+dy] == False:
                visited[x+dx][y+dy] = True
                distance[x+dx][y+dy] = distance[x][y]+1
                deq.append((x+dx, y+dy))
    return distance


def s_bfs(node):
    nx, ny = node
    deq.append(node)
    Visited = [[False for i in range(W)] for j in range(H)]
    Visited[nx][ny] = True
    distance = [[float("inf") for i in range(W)] for j in range(H)]
    distance[nx][ny] = 0
    while deq:
        x, y = deq.popleft()
        for dx, dy in dif:
            if 0 <= x+dx < H and 0 <= y+dy < W and Map[x+dx][y+dy] == "." and Visited[x+dx][y+dy] == False:
                Visited[x+dx][y+dy] = True
                distance[x+dx][y+dy] = distance[x][y]+1
                deq.append((x+dx, y+dy))
    return distance


ans = 1
roads = deque()
for i in range(H):
    for j in range(W):
        if Map[i][j] == ".":
            roads.append((i, j))

while roads:
    x, y = roads.popleft()
    if visited[x][y] == False:
        B = s_bfs((x, y))
        s = -1
        choice=[]
        most_far_distance = 0
        for i in range(H):
            for j in range(W):
                if B[i][j] != float("inf") and B[i][j] > most_far_distance:
                    most_far_distance = B[i][j]
        for i in range(H):
            for j in range(W):
                if B[i][j] == most_far_distance:
                    choice.append((i, j))

        for s in choice:
            C = s_bfs(s)
            for i in range(H):
                for j in range(W):
                    if C[i][j] != float("inf"):
                        ans = max(ans, C[i][j])
print(ans)
