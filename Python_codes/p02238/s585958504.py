n = int(input())
G = []
checked = [False for i in range(n + 1)]
d = [0 for i in range(n + 1)]
f = [0 for i in range(n + 1)]
G.append([])
for i in range(n):
    u, k, *v = map(int, input().split())
    G.append(v)

timestamp = 1

def dfs(id):
    global timestamp

    checked[id] = True
    d[id] = timestamp
    timestamp += 1
    for v in G[id]:
        if not checked[v]:
            dfs(v)
    f[id] = timestamp
    timestamp += 1

for id in range(1, n + 1):
    if not checked[id]:
        dfs(id)

for i in range(1, n + 1):
    print("{0} {1} {2}".format(i, d[i], f[i]))