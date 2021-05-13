from sys import stdin

d_num = int(stdin.readline().strip())

graph = [[] for _ in range(d_num+1)]
for _ in range(d_num):
    u, k, *neighbors = map(int, stdin.readline().split())
    for v in neighbors:
        graph[u].append(v)

visited = set()
timestamps = [None for _ in range(d_num+1)]

def dfs(u, stmp):
    visited.add(u)
    entry = stmp

    stmp += 1
    for v in graph[u]:
        if v not in visited:
            stmp = dfs(v, stmp)

    timestamps[u] = entry, stmp
    return stmp+1

stmp = 1
for v in range(1, d_num+1):
    if v not in visited: stmp = dfs(v, stmp)

for num, (entry, leave) in enumerate(timestamps[1:], 1):
    print(num, entry, leave)