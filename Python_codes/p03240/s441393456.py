n=int(input())

hxy=[]
for _ in range(n):
    x,y,h=map(int,input().split())
    hxy.append([h,x,y])

hxy.sort()

for cx in range(101):
    for cy in range(101):
        flag=0
        temp=hxy[-1]
        H=temp[0]+abs(temp[1]-cx)+abs(temp[2]-cy)

        for item in hxy:
            h=item[0]
            x=item[1]
            y=item[2]
            if h!=max(H-abs(x-cx)-abs(y-cy),0):
                flag=1
                break
        
        if flag==0:
            print(cx,cy,H)
            exit()
