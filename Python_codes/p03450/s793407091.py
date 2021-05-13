from collections import deque

n, m = map(int, input().split())
info = [[] for _ in range(n)]
visited = [0] * n
dist = [0] * n
ans = 'Yes'
for i in range(m):
    l, r, D = map(int, input().split())
    info[l-1].append([r-1, D])
    info[r-1].append([l-1, -D])

for i in range(n):
    if visited[i]:
        continue
    q = deque()
    q.append(i)
    while q:
        p = q.pop()
        for x, d in info[p]:
            if visited[x] == 0:
                visited[x] = 1
                dist[x] = dist[p] + d
                q.append(x)
            elif dist[x] != dist[p] + d:
                ans = 'No'

print(ans)