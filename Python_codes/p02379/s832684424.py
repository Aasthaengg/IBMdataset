def dist(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

x1, y1, x2, y2 = map(float, input().split())
print(dist(x1, y1, x2, y2))
