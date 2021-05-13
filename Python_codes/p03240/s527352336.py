n = int(input())
xyh = []
for i in range(n):
    xyh.append(list(map(int,input().split())))
H = []
for cx in range(0,101):
    for cy in range(0,101):
        hantei = False
        for i in range(n):
            if xyh[i][2] > 0:
                if not H:
                    H.append(xyh[i][2] + abs(cx-xyh[i][0]) + abs(cy-xyh[i][1]))
                else:
                    hantei = True
                    if xyh[i][2] + abs(cx-xyh[i][0]) + abs(cy-xyh[i][1]) != H[0]:
                        H.pop(0)
                        break
        else:
            if hantei: 
                print(cx,cy,H[0])
                exit()
else:
    mx = 0
    for i in range(n):
        if mx < xyh[i][2]:
            ansind = i
            mx = xyh[i][2]
    print(xyh[ansind][0],xyh[ansind][1],xyh[ansind][2])
