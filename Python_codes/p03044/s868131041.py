import sys
sys.setrecursionlimit(1000000)

n = int(input())
t = [[] for _ in range(n)]
color = [None for _ in range(n)]
visited = [False for _ in range(n)]


def dfs(n_num):
    visited[n_num] = True
    for i in t[n_num]:
        if visited[i[0]]:
            continue
        if i[1] % 2 == 0:
            color[i[0]] = color[n_num]
        else:
            color[i[0]] = abs(color[n_num] - 1)
        dfs(i[0])


for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    t[u] += [(v, w)]
    t[v] += [(u, w)]

color[0] = 0
dfs(0)
for i in color:
    print(i)
