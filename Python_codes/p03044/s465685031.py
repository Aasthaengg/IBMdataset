from collections import deque

n = int(input())

u = [0] * n
v = [0] * n
w = [0] * n

dist = [-1] * n
adj_list = [[] for _ in range(n)]

for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1

    adj_list[u].append([v, w])
    adj_list[v].append([u, w])

q = deque()
dist[0] = 0
q.append(0)

while len(q) > 0:
    node = q.popleft()

    for next, d in adj_list[node]:
        if dist[next] > 0:
            continue

        if dist[next] == -1 or dist[next] > dist[node] + d:
            dist[next] = dist[node] + d
            q.append(next)

for i in range(n):
    if dist[i] % 2 == 0:
        dist[i] = 0
    else:
        dist[i] = 1
    print(dist[i])
