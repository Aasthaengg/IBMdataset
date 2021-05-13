import sys
sys.setrecursionlimit(100000000)

n, m, p = map(int, input().split())
routes =[]
bt = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    routes.append([a, b, -1 * (c - p)])
    bt[b].append(a)

enable = set()
enable.add(n)
for i in range(n):
    for j in range(1, n+1):
        if j in enable:
            for k in bt[j]:
                if not k in enable:
                    enable.add(k)

inf = float('inf')
costs = [inf for _ in range(n+1)]
costs[1] = 0
error = False
for i in range(n):
    for route in routes:
        if route[1] in enable and costs[route[0]] + route[2] < costs[route[1]]:
            costs[route[1]] = costs[route[0]] + route[2]
            if i == n-1:
                error = True
                break
if error == True:
    print(-1)
else:
    print(max(0, -1 * costs[n]))

