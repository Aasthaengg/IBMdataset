from itertools import combinations

N, K = map(int,input().split())
points = []
X = []
Y = []

for _ in range(N):
    x, y = map(int,input().split())
    points.append((x, y))
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()

ans = float('inf')

for x1, x2 in combinations(X, 2):
    for y1, y2 in combinations(Y, 2):
        cnt = 0
        for point in points:
            if x1 <= point[0] <= x2 and y1 <= point[1] <= y2:
                cnt += 1
        if cnt >= K:
            ans = min(ans, (x2 - x1) * (y2 - y1))

print(ans)