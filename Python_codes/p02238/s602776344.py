G = {}
N = int(input())
for _ in range(N):
    L = list(map(int, input().split()))
    G[L[0]] = L[2:]

# print(G)
d = [-1] * N
f = [-1] * N
q = [1]
visited = [False] * N

time = 1


def dfs(v):
    global time
    visited[v-1] = True

    for nv in G[v]:
        if d[nv-1] < 0:
            d[nv-1] = time
            time += 1
        if not visited[nv-1]:
            dfs(nv)

    f[v-1] = time
    time += 1


for i in range(1, N+1):
    if not visited[i-1]:
        d[i-1] = time
        time += 1
        dfs(i)

for i in range(N):
    print(i+1, d[i], f[i])

