from collections import deque

n = int(input())
AA = [deque(list(map(int, input().split()))) for _ in range(n)]

graph = [[] for _ in range(n * n)]


def calc(i, j):
    if j > i:
        i, j = j, i
    return i * n + j


to = [0] * (n * n)
for i in range(n):
    for j in range(n - 2):
        u = calc(i, AA[i][j] - 1)
        v = calc(i, AA[i][j + 1] - 1)
        graph[u].append(v)
        to[v] += 1
start = []
for i in range(n * n):
    if to[i] == 0:
        start.append(i)


def topological_sort(edge_num, graph, start, to):
    topo = []
    cnt = 0
    stack = deque(start)
    while stack:
        v = stack.popleft()
        topo.append(v)
        cnt += 1
        for u in graph[v]:
            to[u] -= 1
            if to[u] == 0:
                stack.append(u)
    return topo, cnt


topo, cnt = topological_sort(n * n, graph, start, to)
if cnt != n * n:
    print(-1)
    exit()
day = [1] * (n * n)
for i in topo:
    for j in graph[i]:
        day[j] = day[i] + 1
print(max(day))
