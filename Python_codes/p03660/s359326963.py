import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

dist = [0] * N
def dfs(u, d, p=-1):
    global dist
    dist[u] = d
    for v in edges[u]:
        if v == p:
            continue
        dfs(v, d + 1, u)
    return dist

dist1 = dfs(0, 0, -1)
dist = [0] * N
dist2 = dfs(N - 1, 0, -1)

cnt = 0
for d1, d2 in zip(dist1, dist2):
    if d1 <= d2:
        cnt += 1
if N - cnt < cnt:
    print("Fennec")
else:
    print("Snuke")