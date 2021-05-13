from decimal import Decimal

N = int(input())

xy = [list(map(Decimal,input().split())) for i in range(N)]

cnt ={}

for i in range(N):
    xi = xy[i][0]
    yi = xy[i][1]

    for j in range(i+1,N):
        xj = xy[j][0]
        yj = xy[j][1]

        x_dif =xi-xj
        y_dif = yi-yj
        if x_dif<0:
            x_dif = -x_dif
            y_dif = -y_dif
        elif x_dif == 0:
            y_dif = abs(y_dif)

        if (x_dif,y_dif)  in cnt.keys():
            cnt[x_dif,y_dif] += 1
        else:
            cnt[x_dif, y_dif] =1

if N == 1:
    print(1)
else: print(N-max(cnt.values()))