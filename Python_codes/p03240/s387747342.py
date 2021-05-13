n=int(input())
xyh=[list(map(int,input().split())) for _ in range(n)]
xyh.sort(key=lambda x:x[2],reverse=True)

for cx in range(0,101):
    for cy in range(0,101):
        x,y,h=xyh[0]
        H=h+abs(x-cx)+abs(y-cy)
        if H<0:
            continue

        for i in range(1,n):
            x,y,h=xyh[i]

            if h!=max(H-abs(x-cx)-abs(y-cy),0):
                break
        else:
            print('{} {} {}'.format(cx,cy,H))
            exit(0)