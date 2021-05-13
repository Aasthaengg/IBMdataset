from itertools import accumulate, combinations

N, K = map(int, input().split())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
cx_to_x = sorted(list(set(X)))
x_to_cx = {k : i for i, k in enumerate(cx_to_x)}
cy_to_y = sorted(list(set(Y)))
y_to_cy = {k : i for i, k in enumerate(cy_to_y)}
nx = len(cx_to_x)
ny = len(cy_to_y)
points = [[0] * nx for _ in range(ny)]
for x, y in zip(X, Y):
    points[y_to_cy[y]][x_to_cx[x]] += 1
cum = [[0] * (nx+1)] + [list(accumulate([0] + row)) for row in points]
for i in range(1, ny+1):
    for j in range(nx+1):
        cum[i][j] += cum[i-1][j]
ans = float('inf')
for x1, x2 in combinations(range(nx), 2):
    for y1, y2 in combinations(range(ny), 2):
        cnt = cum[y2+1][x2+1] - cum[y2+1][x1] - cum[y1][x2+1] + cum[y1][x1]
        if cnt >= K:
            area = (cx_to_x[x2] - cx_to_x[x1]) * (cy_to_y[y2] - cy_to_y[y1])
            ans = min(ans, area)
print(ans)