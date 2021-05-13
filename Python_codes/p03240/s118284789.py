N = int(input())
XYH = []
for i in range(N):
    XYH.append(list(map(int,input().split())))

flag=0
for Cx in range(101):
    for Cy in range(101):
        Hcands = []
        for i in range(N):
            X = XYH[i][0]
            Y = XYH[i][1]
            h = XYH[i][2]
            if h>0:
                Hcand = abs(Cx-X)+abs(Cy-Y)+h
                break
        for i in range(N):
            X = XYH[i][0]
            Y = XYH[i][1]
            h = XYH[i][2]
            if h != max(Hcand-abs(Cx-X)-abs(Cy-Y), 0):
                flag=0
                break
            else:
                flag=1
        if flag==1:
            print(Cx,Cy,Hcand)
            break
    if flag==1:
        break