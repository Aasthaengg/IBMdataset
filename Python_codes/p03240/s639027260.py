N, *XYH = map(int, open(0).read().split())
XYH = [(x, y, h) for x, y, h in zip(*[iter(XYH)] * 3)]
pos_i = -1
for i, (_, _, h) in enumerate(XYH):
    if h > 0:
        pos_i = i
        break
for i in range(101):
    for j in range(101):
        t_x, t_y, t_h = XYH[pos_i]
        tmp_summit = t_h + abs(i - t_x) + abs(j - t_y)
        for x, y, h in XYH:
            if h > 0 and tmp_summit - h != abs(i - x) + abs(j - y):
                break
            elif h == 0 and tmp_summit > abs(i - x) + abs(j - y):
                break
        else:
            print(i, j, tmp_summit)
            exit()
