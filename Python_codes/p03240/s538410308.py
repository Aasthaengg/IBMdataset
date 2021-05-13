N = int(input())

XYH = [list(map(int, input().split())) for _ in range(N)]


for cx in range(0, 101):
    for cy in range(0, 101):

        prev = None
        flg = False
        zeros = []
        for x, y, h in XYH:
            if h == 0:
                zeros.append((x, y, h))
                continue

            cur_h = h + abs(x - cx) + abs(y - cy)

            if prev is not None:
                if prev != cur_h:
                    flg = True
                    break

            prev = cur_h

        if not flg:
            for x, y, h in zeros:
                if max(0, cur_h - abs(x - cx) - abs(y - cy)) != 0:
                    flg = True
                    break

            if not flg:
                print(cx, cy, cur_h)
                exit()

