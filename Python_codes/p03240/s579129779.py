n = int(input())
coord = []

for i in range(n):
    x, y, h = map(int, input().split())
    coord.append([h, x, y])
    if h > 0:
        x0, y0, h0 = x, y, h

flag = False


for cx in range(0, 101):
    for cy in range(0, 101):
        flag = True

        H = h0 + abs(x0 - cx) + abs(y0 - cy)

        for i in range(n):
            if coord[i][0] != max(H - abs(coord[i][1] - cx) - abs(coord[i][2] - cy), 0):
                flag = False
                break

        if flag is True:
            res_x = cx
            res_y = cy
            res_h = H

print(res_x, res_y, res_h)
