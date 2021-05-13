n = int(input())
xyh = []
for i in range(n):
    temp = list(map(int,input().split()))
    if temp[2] > 0:
        x,y,h = temp[0],temp[1],temp[2]
    xyh.append(temp)
for i in range(101):
    for j in range(101):
        for k in xyh:
            if k[2] > 0 and k[2]+abs(k[0]-j)+abs(k[1]-i) != h+abs(x-j)+abs(y-i):
                break
            elif k[2]+abs(k[0]-j)+abs(k[1]-i) < h+abs(x-j)+abs(y-i):
                break
        else:
            print(j,i,h+abs(x-j)+abs(y-i))
            exit()