from collections import deque
N, M = map(int,input().split())
graph = [[] for i in range(N + 1)]
dist = [-1] * (N + 1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dist[1] = 1
q = deque([1])
while q:
    x = q.popleft()
    for j in graph[x]:
        if dist[j] == -1:
            q.append(j)
            dist[j] = x
ans = dist[2:]
if -1 in ans:
    print("No")
else:
    print("Yes")
    print(*ans, sep = "\n")