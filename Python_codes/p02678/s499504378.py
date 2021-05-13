n, m = map(int, input().split())
path = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

q = [1]
visited = [-1] * (n + 1)

visited[1] = 0
while q:
    node = q.pop(0)
    for i in path[node]:
        if visited[i] == -1:
            q.append(i)
            visited[i] = node

if any([True for v in visited[2:] if v == -1]):
    print("No")
else:
    print("Yes")
    for v in visited[2:]:
        print(v)
