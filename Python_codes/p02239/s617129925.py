from collections import deque

n = int(input())
graphs = [[] for i in range(n+1)]
visited = [False] * (n+1)
min_s = [-1] * (n+1)

for i in range(1, n+1):
    nodes = list(map(int, input().split()))
    graphs[i].extend(nodes[1:])

q = deque()
q.append([1, 0])
while q:
    node, j = q.popleft()
    if not visited[node]:
        visited[node] = True
        min_s[node] = j
    nodes = graphs[node]
    for node in nodes:
        if not visited[node]:
            q.append([node, j+1])

for i in range(1, n+1):
    print(i, min_s[i])
