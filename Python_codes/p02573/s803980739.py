from collections import deque

n, m = map(int, input().split())

#graph = [[] for _ in range(n+1)]
graph = [set() for _ in range(n+1)]


for i in range(m):
    a, b = map(int, input().split())
#    graph[a].append(b)
#    graph[b].append(a)
    graph[a].add(b)
    graph[b].add(a)


dist = [-1] * (n+1)
dist[0] = 0


d = deque()
ans = 1
for j in range(len(dist)):
    if dist[j] != -1:
        continue
    d.append(j)
    cnt = 0
    while d:
        v = d.popleft()
        for i in graph[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)
            cnt = cnt + 1
    ans = max(ans,cnt)

print(ans)
