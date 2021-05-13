n=int(input())
xyh=[list(map(int,input().split())) for i in range(n)]
xyh.sort(key=lambda x:x[2],reverse=True)
for X in range(0,101):
    for Y in range(0,101):
        f=True
        H=xyh[0][2]+abs(xyh[0][0]-X)+abs(xyh[0][1]-Y)
        for i in range(1,n):
            x,y,h=xyh[i]
            if h==0:
                if H-abs(x-X)-abs(y-Y)>0:
                    f=False
                    break
            else:
                if H-abs(x-X)-abs(y-Y)!=h:
                    f=False
                    break
        if f:
            print(X,Y,H)
            break