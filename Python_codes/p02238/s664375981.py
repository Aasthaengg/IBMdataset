from collections import defaultdict


def dfs(v, t):
    if start[v] == 0:
        start[v] = t
        t += 1
    else:
        return t

    for nv in graph[v]:
        t = dfs(nv, t)

    end[v] = t
    t += 1

    return t


n = int(input())

graph = defaultdict(list)

for _ in range(n):
    u, k, *v = map(int, input().split())
    for v in v:
        graph[u].append(v)

start = [0] * (n + 1)
end = [0] * (n + 1)


t = 1

for i in range(1, n + 1):
    t = dfs(i, t)

for i in range(1, n + 1):
    print(i, start[i], end[i])
