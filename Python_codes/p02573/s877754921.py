from collections import deque

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]


t = dict()

for i in range(1, n + 1):
    t[i] = set()


for a, b in ab:
    t[a].add(b)
    t[b].add(a)


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)

            stack.extend(graph[vertex] - visited)
    return visited

seen = set()
length = 0
for i in range(1, n+1):
    if i not in seen:
        ans = dfs(t, i)
        for num in ans:
            seen.add(num)

        if len(ans) > length:
            length = len(ans)

print(length)