from collections import deque

def bfs(start, g, visited):
    q = deque([start])
    visited[start] = 0
    while q:
        curr_node = q.popleft()
        for next_node, w in g[curr_node]:
            if visited[next_node] >= 0: continue
            visited[next_node] = (visited[curr_node] + w)%2
            q.append(next_node)


n = int(input())
gl = [ [] for _ in range(n+1)]
for _ in range(n-1):
    u,v,w = map(int, input().split())
    gl[u].append((v,w))
    gl[v].append((u,w))
visited = [-1] * (n+1)
bfs(1, gl, visited)

for v in visited[1:]:
    if v%2 == 0: print(0)
    else: print(1)