from collections import deque

n = int(input())

distance = [-1] * n

edge = [dict() for _ in range(n)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    edge[u][v] = w
    edge[v][u] = w

D = deque([0])
distance[0] = 0

while D:
    now = D.popleft()
    for i in edge[now]:
        if distance[i] == -1:
            distance[i] = (distance[now] + edge[now][i]) % 2
            D.append(i)

for i in distance:
    print(i)