N = int(input())

nodes = [tuple(map(int, input().split(' '))) for _ in range(N)]
d = [-1 for _ in range(N + 1)]
f = [-1 for _ in range(N + 1)]

clock = 0


def dfs(node):
    global clock
    if d[node] == -1:
        clock += 1
        d[node] = clock
    neighbors = sorted(nodes[node - 1][2:])

    for neighbor in neighbors:
        if d[neighbor] == -1:
            dfs(neighbor)

    if f[node] == -1:
        clock += 1
        f[node] = clock


for i in range(1, N + 1):
    dfs(i)
    print(i, d[i], f[i])

