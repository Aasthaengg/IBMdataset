import sys
sys.setrecursionlimit(1000000)

N = int(input())

G = {k: [] for k in range(N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    # 無向グラフ
    G[a].append(b)
    G[b].append(a)


def dfs(v, p, c, distance):  # 現在の頂点v, vの親p, 現在の距離c
    distance[v] = c
    for nv in G[v]:
        if visited[nv] is False:
            if nv == p:
                continue
            dfs(nv, v, c+1, distance)
    return


distance_f = [-1]*(N+1)
visited = [False] * (N+1)
dfs(1, -1, 0, distance_f)

distance_s = [-1]*(N+1)
visited = [False] * (N+1)
dfs(N, -1, 0, distance_s)

# print(distance_f)
# print(distance_s)

c = 0
for i in range(2, N):
    if distance_f[i] <= distance_s[i]:
        c += 1
    elif distance_f[i] > distance_s[i]:
        c -= 1

if c > 0:
    print('Fennec')
elif c <= 0:
    print('Snuke')
