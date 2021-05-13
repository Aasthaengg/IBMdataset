import sys

sys.setrecursionlimit(10 ** 8)
n = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(lambda x: x - 1, list(map(int, input().split()))[2:]))

timestamp = [[] for _ in range(n)]
visited = [False] * n
cnt = 0


def dfs(v):
    global visited
    global cnt
    global timestamp
    cnt += 1
    timestamp[v].append(cnt)
    visited[v] = True
    for to in graph[v]:
        if visited[to]:
            continue
        else:
            dfs(to)
    cnt += 1
    timestamp[v].append(cnt)


dfs(0)

while False in visited:
    nxt = visited.index(False)
    dfs(nxt)


for i, (d, f) in enumerate(timestamp, 1):
    print(i, d, f)

