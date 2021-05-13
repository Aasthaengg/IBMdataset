from collections import deque
n = int(input())
to = [[] for _ in range(n)]
for i in range(n-1):
    u, v, w = map(int, input().split())
    u , v = u-1, v-1
    to[u].append([v, w])
    to[v].append([u, w])
color = [-1] * n
color[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    for u, w in to[v]:
        if color[u] != -1:
            continue
        if w % 2 != 0:
            color[u] = color[v] ^ 1
        else:
            color[u] = color[v]
        q.append(u)
for c in color:
    print(c)