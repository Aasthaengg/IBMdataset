n = int(input())
L = []
for _ in range(n):
    x, y, h = map(int, input().split())
    if h > 0:
        sx, sy, sh = x, y, h
    L.append((x, y, h))
for cy in range(101):
    for cx in range(101):
        d = abs(sx - cx) + abs(sy - cy)
        H = sh + d
        for x, y, h in L:
            if h == 0:
                if H > abs(x - cx) + abs(y - cy):
                    break
            else:
                if H - abs(x - cx) - abs(y - cy) != h:
                    break
        else:
            print(cx, cy, H)
            exit()
