N = int(input())
xyh = [list(map(int, input().split())) for i in range(N)]

for Cx in range(101):
    for Cy in range(101):
        criteria = -1
        ax, ay, ah = 0, 0, 0
        cnt = 0
        for x, y, h in xyh:
            if h == 0:
                continue
            H = h + abs(x - Cx) + abs(y - Cy)
            if H == criteria or criteria == -1:
                criteria = H
                ax, ay, ah = x, y, h
                cnt += 1
                continue
            else:
                break
        else:
            if cnt == 1:
                print(ax, ay, ah)
                exit()
            else:
                print(Cx, Cy, criteria)
