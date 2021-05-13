import sys
sys.setrecursionlimit(4100000)
N, M = map(int, input().split())
graph = [[] * N for _ in range(N)]
for _ in range(M):
    L, R, D = map(int, input().split())
    L -= 1
    R -= 1
    graph[L].append((R, D))
    graph[R].append((L, -D))


def dfs(node, dist):
    global visited
    global dists
    dists[node] = dist
    for next, d in graph[node]:
        if next in visited:
            if d + dist != dists[next]:
                print('No')
                sys.exit()
        else:
            visited.add(next)
            dfs(next, dist + d)


visited = set()
dists = [0] * N
for i in range(N):
    if i in visited:
        continue
    visited.add(i)
    dfs(i, 0)

print('Yes')
