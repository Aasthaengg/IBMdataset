from itertools import combinations

n, k = (int(x) for x in input().split())
XY = [tuple(int(x) for x in input().split()) for _ in range(n)]

ans = 10**20
X = []
Y = []
for x, y in XY:
    X.append(x)
    Y.append(y)

ans = 10**20
for ax, bx in combinations(X, 2):
    if ax > bx:
        ax, bx = bx, ax
    for ay, by in combinations(Y, 2):
        if ay > by:
            ay, by = by, ay
        count = 0
        for x, y in XY:
            if ax <= x <= bx and ay <= y <= by:
                count += 1
        if count >= k:
            ans = min(ans, (bx - ax) * (by - ay))

print(ans)
