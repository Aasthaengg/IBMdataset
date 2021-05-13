N = int(input())

XYH = []
for _ in range(N):
    x, y, h = map(int, input().split())
    XYH.append((x, y, h))
XYH.sort(key=lambda x: -x[2])

for Cx in range(0, 101):
    for Cy in range(0, 101):
        flg = True

        if XYH[0][2] == 0:
            Ch = 1
        else:
            Ch = XYH[0][2]+abs(XYH[0][0]-Cx)+abs(XYH[0][1]-Cy)

        for x, y, h in XYH:
            if h != max(Ch - abs(x-Cx) - abs(y-Cy), 0):
                flg = False

        if flg:
            print(Cx, Cy, Ch)
            exit()
