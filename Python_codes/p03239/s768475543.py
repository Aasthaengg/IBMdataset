N, T = map(int, input().split())
costs = []
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T:
        costs.append(c)

if costs:
    costs.sort()
    ans = costs[0]
else:
    ans = 'TLE'
print(ans)
