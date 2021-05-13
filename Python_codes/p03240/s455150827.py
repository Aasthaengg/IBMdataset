n = int(input())
XYH = [list(map(int, input().split())) for _ in range(n)]
XYH.sort(key=lambda x:x[2])
X, Y, H = XYH[-1]
for cx in range(101):
    for cy in range(101):
        h = H + abs(cx-X) + abs(cy-Y)
        flag = False
        for xyh in XYH:
            if xyh[2] != max(h-abs(cx-xyh[0])-abs(cy-xyh[1]), 0):
                flag = True
        if flag: continue
        print(cx, cy, h)