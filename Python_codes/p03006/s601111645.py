n = int(input())
xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))
dxdy = {}
if n==1:
    print(1)
    exit()
for i in range(n-1):
    for j in range(i+1, n):
        dx = xy[i][0] - xy[j][0]
        dy = xy[i][1] - xy[j][1]
        if dx<0:
            dx, dy = -dx, -dy
        elif dx==0:
            dx, dy = dx, abs(dy)
        if (dx, dy) in dxdy:
            dxdy[(dx, dy)] += 1
        else:
            dxdy[(dx, dy)] = 1
print(n-max(dxdy.values()))