from collections import deque
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

count = 0
for i in range(m):
    edges = [[]*n for _ in range(n)]
    for j in range(m):
        if j == i:
            continue
        edges[ab[j][0]-1].append(ab[j][1]-1)
        edges[ab[j][1]-1].append(ab[j][0]-1)
    #print(edges)
    d = deque([0])
    visited = [0]*n
    visited[0] = 1
    while d:
        p = d.pop()
        for child in edges[p]:
            if visited[child] == 1:
                continue
            visited[child] = 1
            d.append(child)
    if sum(visited) != n:
        count += 1
print(count)

