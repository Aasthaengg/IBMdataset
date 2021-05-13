import sys
import bisect

inf = 10**15
mod = 10**9+7

def getH(Cx, Cy, x, y, h):
    return h + abs(x-Cx) + abs(y-Cy)

inf = 10**15
mod = 10**9+7
n = int(input())
Hinfo = [list(map(int, input().split())) for i in range(n)]
H = -1
Hmax = inf
for Cx in range(101):
    for Cy in range(101):
        H = -1
        flag = True
        for tmp in Hinfo:
            x,y,h = tmp
            if h == 0:
                Hmax = getH(Cx, Cy, x, y, h)
            else:
                canH = getH(Cx, Cy, x, y, h)
                if H > 0:
                    if H != canH:
                        flag = False
                        break
                else:
                    H = canH
            if Hmax < H:
                flag = False
                break
        if Hmax >= H and flag:
            print('{} {} {}'.format(Cx, Cy, H))
            sys.exit()