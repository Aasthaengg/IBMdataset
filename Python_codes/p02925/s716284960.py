import sys
sys.setrecursionlimit(500000)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
vs = n * (n - 1) // 2

vmap = {}
c = 0
for i in range(n):
    for j in range(i):
        vmap[(i, j)] = c
        vmap[(j, i)] = c
        c += 1

edges = [[] for _ in range(vs)]
numin = [0] * vs
for i in range(n):
    for j in range(n - 2):
        j1 = a[i][j] - 1
        j2 = a[i][j + 1] - 1
        edges[vmap[(i, j1)]].append(vmap[(i, j2)])
        numin[vmap[(i, j2)]] += 1

order = []
day = [1] * vs
q = [i for i in range(vs) if numin[i] == 0]
while len(q) > 0:
    index = q.pop(0)
    order.append(index)
    d = day[index]
    for i in edges[index]:
        numin[i] -= 1
        if numin[i] == 0:
            q.append(i)
            day[i] = max(day[i], d + 1)

print(max(day) if len(order) == vs else -1)
