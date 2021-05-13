from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

def dfs(now, prev):
    for nxt, w in edge[now]:
        if nxt == prev:
            continue
        
        dist[nxt] = dist[now] + w
        dfs(nxt, now)


n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    edge[u-1].append([v-1, w])
    edge[v-1].append([u-1, w])

dist = [0] * n
dfs(0, -1)

for d in dist:
    if d % 2 == 0:
        print(0)
    else:
        print(1)