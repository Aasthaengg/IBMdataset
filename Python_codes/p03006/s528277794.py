N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]

li = {}
for i in range(N):
    for j in range(N):
        if i==j:
            continue

        x1,y1 = XY[i][0],XY[i][1]
        x2,y2 = XY[j][0],XY[j][1]

        mm1 = x2-x1
        mm2 = y2-y1
        # if mm1<0 and mm2<0:
        #     mm1 *= -1
        #     mm2 *= -1
        PQ = (mm1, mm2)

        if PQ in li:
            li[PQ] += 1
        else:
            li[PQ] = 1

mm = 0
for i in li:
    mm = max(mm,li[i])
print(N-mm)