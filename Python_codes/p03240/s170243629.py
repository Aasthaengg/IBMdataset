def dis(xi, xj, yi, yj):
    return abs(xi - xj) + abs(yi - yj)
n = int(input())
coords = [tuple(map(int, input().split())) for _ in range(n)]
grids = [(i, j) for i in range(101) for j in range(101)]
for x, y, h in coords:
    if h > 0:
        break    
for xj, yj in grids:
    flag = True
    base = dis(x, xj, y, yj) + h
    for xi, yi, hi in coords:
        if hi != max(base-abs(xi-xj)-abs(yi-yj), 0):
            flag = False
    if flag:
        break
print(xj, yj, dis(x, xj, y, yj) + h)