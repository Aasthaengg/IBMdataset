N = int(input())
XYH = [[0, 0, 0] for _ in range(N)]
for i in range(N):
    XYH[i] = list(map(int, input().split()))

XYH.sort(key = lambda x: x[2], reverse = True)
for x in range(101):
    for y in range(101):
        diff_x = abs(XYH[0][0] - x)
        diff_y = abs(XYH[0][1] - y)
        H = XYH[0][2] + diff_x + diff_y
        for xyh in XYH[1:]:
            if xyh[2] != max(H - abs(xyh[0] - x) - abs(xyh[1] - y), 0):
                break
        else:
            print(x, y, H)
            exit()
