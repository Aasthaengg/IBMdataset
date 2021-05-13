from collections import deque

N = int(input())
edge = [[] for i in range(N)]
color = [-1] * N

for i in range(N-1):
    u, v, w = map(int, input().split())
    edge[u-1].append((v-1, w))
    edge[v-1].append((u-1, w))

q = deque([])
q.append((0,0))

while(q):
    cur, col = q.popleft()
    color[cur] = col
    for next, weight in edge[cur]:
        if color[next] != -1:
            continue

        if weight % 2:
            q.append((next, 1-col))
            color[next] = 1-col
        else:
            q.append((next, col))
            color[next] = col

print(*color, sep="\n")