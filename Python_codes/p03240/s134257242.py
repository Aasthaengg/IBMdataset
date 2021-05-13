n=int(input())
xyh=sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: -x[2])

for cx in range(0,101):
    for cy in range(0,101):
        flag=True
        h=abs(cx-xyh[0][0])+abs(cy-xyh[0][1])+xyh[0][2]
        for i in range(n):
            if max(h-abs(cx-xyh[i][0])-abs(cy-xyh[i][1]), 0)!=xyh[i][2]:
                flag=False
        if flag:
            print(cx,cy,h)
            exit()

