from sys import setrecursionlimit as SRL, stdin
inf = 10**15
SRL(10 ** 7)
rd = stdin.readline
rrd = lambda: map(int, rd().strip().split())

n, m, l = rrd()
dis = [[inf] * 305 for _i in range(305)]
need = [[inf] * 305 for _i in range(305)]
for i in range(n):
    dis[i][i] = 0
for i in range(m):
    a, b, c = rrd()
    dis[a][b] = c
    dis[b][a] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            need[i][j] = 0
        elif dis[i][j] <= l:
            need[i][j] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            need[i][j] = min(need[i][j], need[i][k] + need[k][j])
q = int(input())

while q:
    s, t = rrd()
    if need[s][t] < inf:
        print(need[s][t]-1)
    else:
        print(-1)
    q -= 1








