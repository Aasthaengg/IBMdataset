n, m = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

alist = [[] for _ in range(3*n)]
for u, v in uv:
    u, v = u-1, v-1
    alist[u].append(n+v)
    alist[n+u].append(2*n+v)
    alist[2*n+u].append(v)


# BFS
queue = [s-1]
visited = [-3]*(3*n)
visited[s-1] = 0
while len(queue) > 0:
    q = queue.pop(0)
    for v in alist[q]:
        if visited[v] < 0:
            queue.append(v)
            visited[v] = visited[q] + 1
print(visited[t-1]//3)


