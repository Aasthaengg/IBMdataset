from collections import deque

n = int(input())

color = [-1]*(n+1)
rel = [{} for i in range(n+1)]

for i in range(n-1):
    u, v, w = map(int, input().split())
    rel[u][v] = rel[v][u] = w

def f(n):
    color[n] = 0
    stack = deque()
    stack.append(n)
    while stack:
        new = stack.pop()
        for ver in rel[new]:
            if color[ver] == -1:
                color[ver] = 1-color[new] if rel[new][ver]&1 else color[new]
                stack.append(ver)

for i in range(1, n+1):
    if color[i] != -1: continue
    f(n)

print(*color[1:], sep="\n")
