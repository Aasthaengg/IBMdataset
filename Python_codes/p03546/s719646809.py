h, w = map(int, input().split())
INF = 10**9
costs = [list(map(int, input().split())) for _ in range(10)]
for k in range(10):
    for j in range(10):
        for i in range(10):
            if costs[i][j] > costs[i][k] + costs[k][j]:
                costs[i][j] = costs[i][k] + costs[k][j]
opt_costs = [costs[i][1] for i in range(10)]
ans = 0
for _ in range(h):
    a = list(map(int, input().split()))
    for v in a:
        if v > -1:
            ans += opt_costs[v]
print(ans)

