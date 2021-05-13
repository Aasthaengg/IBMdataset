n=int(input())
xyh=[list(map(int,input().split())) for _ in range(n)]
xyh=sorted(xyh, key=lambda x:x[2], reverse=True)

for xi in range(101):
    for yi in range(101):
        hi=0
        flag=True
        for i in range(n):
            x=xyh[i][0]
            y=xyh[i][1]
            h=xyh[i][2]
            if i==0:
                hi=abs(xi-x)+abs(yi-y)+h
            if max(hi-abs(xi-x)-abs(yi-y),0)!=h:
                flag=False
        if flag:
            print(xi, yi, hi)
            break
    else:
        continue
    break