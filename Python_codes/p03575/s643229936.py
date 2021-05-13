from collections import deque
import copy

n, m = map(int, input().split())
arr = [[False] * 60 for x in range(60)]
ab = []

for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = True
    arr[b - 1][a - 1] = True
    ab.append([a - 1, b - 1])


def dfs(x):
    if visited[x]:
        return
    else:
        visited[x] = True
        for i in range(n):
            if graph[x][i]:
                dfs(i)


connected = [True] * m
for i in range(m):
    graph = copy.deepcopy(arr)
    graph[ab[i][0]][ab[i][1]] = False
    graph[ab[i][1]][ab[i][0]] = False
    visited = [False] * 60
    dfs(0)

    for j in range(n):
        if not visited[j]:
            connected[i] = False
            break


print(m - sum(connected))