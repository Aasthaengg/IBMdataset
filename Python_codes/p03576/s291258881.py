import sys

N, K = map(int, sys.stdin.readline().split())
points = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

area = float("inf")
x_sorted = sorted(points)
y_sorted = sorted(points, key = lambda x: x[1])
for i1 in range(N-1):
    for i2 in range(i1+1, N):
        for j1 in range(N-1):
            for j2 in range(j1+1, N):
                x_min = x_sorted[i1][0]
                x_max = x_sorted[i2][0]
                y_min = y_sorted[j1][1]
                y_max = y_sorted[j2][1]
                num = 0
                for i in range(N):
                    if x_min <= points[i][0] <= x_max and y_min <= points[i][1] <= y_max:
                        num += 1
                tmp_area = (x_max - x_min) * (y_max - y_min)
                if num >= K and tmp_area < area:
                    area = tmp_area
                
print(area)