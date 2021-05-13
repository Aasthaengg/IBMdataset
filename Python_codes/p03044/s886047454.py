n = int(input())
edge = [[int(i) for i in input().split()] for j in range(n-1)]
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    u, v, w = edge[i][0], edge[i][1], edge[i][2] % 2
    graph[u].append((v,w))
    graph[v].append((u,w))

color = [-1] * (n+1)
dist = [0] * (n+1)    
stack = [1]
color[1] = 0

while stack:
    x = stack.pop()
    cx = color[x]
    dx = dist[x]
    for y, w in graph[x]:
        if color[y] >= 0:
            continue
        dist[y] = dist[x] + w
        if dist[x] ^ dist[y] == 0:
            color[y] = color[x]
        else:
            color[y] = (color[x] + 1) % 2
        stack.append(y)
print('\n'.join([str(n) for n in color[1:]]))