import numpy as np

n, m, x = map(int, input().split())
a = []
cost = []
for _ in range(n):
    inp = input().split()
    cost.append(int(inp[0]))
    a.append(
        np.array(
            list(map(int, inp[1:]))
        )
    )

ans = -1
for i in range(2 ** n):
    total = 0
    skill = np.zeros(m)
    for j in range(n):
        if (i >> j) & 1:
            total += cost[j]
            skill += a[j]
    if (all(skill >= x)):
        if (ans == -1):
            ans = total
        else:
            ans = min(ans, total)

print(ans)