from operator import itemgetter
N = int(input())
XYZ = [list(map(int, input().split())) for _ in range(N)]

XYZ.sort(key=itemgetter(2), reverse=True)

for x in range(101):
    for y in range(0, 101):
        H = XYZ[0][2]+abs(XYZ[0][0]-x)+abs(XYZ[0][1]-y)
        judge = True
        for xyz in XYZ[1:]:
            if xyz[2] == max(H-abs(xyz[0]-x)-abs(xyz[1]-y),0):
                pass
            else:
                judge = False
                break
        if judge:
            X = x
            Y = y
            break
    if judge:
        break
print(X, Y, H)