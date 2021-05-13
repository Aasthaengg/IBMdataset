import sys
input = sys.stdin.readline

n,c = map(int, input().split())
color = []
for _ in range(c):
    color.append(list(map(int, input().split())))

grid = {i:{} for i in range(3)}
for i in range(n):
    for j,t in enumerate(map(int, input().split())):
        t -= 1
        if t not in grid[(i+j + 2) % 3]:
            grid[(i+j + 2) % 3][t] = 0
        grid[(i+j + 2) % 3][t] += 1

costs = [[0 for _ in range(c)],[0 for _ in range(c)],[0 for _ in range(c)]]
for cc in range(c):
    for i in range(3):
        for d,cnt in grid[i].items():
            costs[i][cc] += color[d][cc] * cnt

rc = range(c)
x = sorted(list(rc), key=lambda x: costs[0][x])[:3]
y = sorted(list(rc), key=lambda x: costs[1][x])[:3]
z = sorted(list(rc), key=lambda x: costs[2][x])[:3]

mn = 10**9
for i in x:
    for j in y:
        for k in z:
            if i == j or j == k or k == i:
                continue
            if mn > costs[0][i] + costs[1][j] + costs[2][k]:
                mn = costs[0][i] + costs[1][j] + costs[2][k]
print(mn)