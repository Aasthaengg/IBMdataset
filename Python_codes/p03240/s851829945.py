import sys
N = int(input())

XYH = []
for _ in range(N):
    x, y, h = list(map(int, input().split()))
    XYH.append((x, y, h))


for cx in range(101):
    for cy in range(101):
        for xyh in XYH:
            if xyh[2] > 0:
                H = abs(cx - xyh[0]) + abs(cy - xyh[1]) + xyh[2]
                break
        for xyh in XYH:
            _x, _y, _h = xyh
            if _h == max(0, H - abs(cx-_x) - abs(cy-_y)):
                continue
            break
        else:
            print(cx, cy, H)
            sys.exit(0)
