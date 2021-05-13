N = int(input())
xyh = []
si = 0
for i in range(N):
    x, y, h = map(int, input().split())
    xyh.append([x,y,h])
    if h > 0:
        si = i

for cx in range(101):
    for cy in range(101):
        H = xyh[si][2] + abs(cx - xyh[si][0]) + abs(cy - xyh[si][1])
        ok = True
        for x,y,h in xyh:
            if h > 0 and H - h != abs(cx - x) + abs(cy - y):
                ok = False
            if h == 0 and H > abs(cx - x) + abs(cy - y):
                ok = False
        if ok:
            print(cx, cy, H)
            exit()