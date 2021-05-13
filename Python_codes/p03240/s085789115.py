N = int(input())
XYH = []

for _ in range(N):
    xi, yi, hi = map(int, input().split())
    XYH.append((xi, yi, hi))


for cx in range(101):
    for cy in range(101):
        flag = True
        # x0, y0, h0 = XYH[0][0],XYH[0][1],XYH[0][2]
        # prob_H = h0 + abs(x0-cx) + abs(y0-cy)
        for x0, y0, h0 in XYH[0:]:
            prob_H = h0 + abs(x0-cx) + abs(y0-cy)
            if h0 == 0:
                continue
            break
        for xi, yi, hi in XYH[0:]:
            if max(prob_H - abs(xi-cx) - abs(yi-cy),0) == hi:
                continue
            else:
                flag = False
                break
        if flag == False:
            continue

        print(cx,cy,prob_H)
        quit()
