from itertools import accumulate
from operator import add

def getAccAss(Ass):
    accAss = [[0] * (len(Ass[0])+1)] + [accumulate([0] + As) for As in Ass]
    for x in range(1, len(accAss)):
        accAss[x] = list(map(add, accAss[x], accAss[x-1]))
    return accAss
def getRangeSum2D(accAss, xFr, xTo, yFr, yTo):
    return accAss[xTo+1][yTo+1] - accAss[xTo+1][yFr] - accAss[xFr][yTo+1] + accAss[xFr][yFr]

def rec(x1, x2, y1, y2, no):
    num = getRangeSum2D(accAss, x1, x2, y1, y2)
    if num == 1:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                ansss[x][y] = no
        return no
    else:
        yL = -1
        for y in range(y1, y2+1):
            if getRangeSum2D(accAss, x1, x2, y, y) > 0:
                if yL == -1:
                    yL = y
                else:
                    no = rec(x1, x2, y1, yL, no)
                    no = rec(x1, x2, yL+1, y2, no+1)
                    return no
        xL = -1
        for x in range(x1, x2+1):
            if getRangeSum2D(accAss, x, x, y1, y2) > 0:
                if xL == -1:
                    xL = x
                else:
                    no = rec(x1, xL, y1, y2, no)
                    no = rec(xL+1, x2, y1, y2, no+1)
                    return no


H, W, K = map(int, input().split())
Sss = [input() for _ in range(H)]
Ass = [[int(S == '#') for S in Ss] for Ss in Sss]

accAss = getAccAss(Ass)

ansss = [[0]*(W) for _ in range(H)]
rec(0, H-1, 0, W-1, 1)

print('\n'.join([' '.join(map(str, anss)) for anss in ansss]))
