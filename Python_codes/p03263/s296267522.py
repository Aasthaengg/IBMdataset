h,w=map(int,input().split())
aa=[list(map(int, input().split())) for _ in range(h)]
odd=[]
for y in range(h):
    temp=[]
    for x in range(w):
        if aa[y][x]%2==1:
            temp.append((y,x))
    if y%2==0:
        temp.sort()
    else:
        temp.sort(reverse=True)
    odd+=temp
#print(odd)
result=[]
i=0
while i<(len(odd)//2)*2:
    #print("i#",i)
    start=odd[i]
    sx,sy=start[1],start[0]

    goal=odd[i+1]
    gx,gy=goal[1],goal[0]

    #print(sx,sy,gx,gy)

    #先に縦移動
    if sy%2==0:
        if gx<sx:
            flag="yx"
        else:
            flag="xy"
    else:
        if gx<sx:
            flag="xy"
        else:
            flag="yx"
    
    while sx!=gx or sy!=gy:
        #print(result)
        if flag=="xy":
            if sx<gx:
                result.append((sy+1,sx+1,sy+1,sx+1+1))
                sx+=1
            elif sx>gx:
                result.append((sy+1,sx+1,sy+1,sx-1+1))
                sx-=1
            elif sy<gy:
                result.append((sy+1,sx+1,sy+1+1,sx+1))
                sy+=1
            else:
                result.append("error1")
        elif flag=="yx":
            if sy<gy:
                result.append((sy+1,sx+1,sy+1+1,sx+1))
                sy+=1
            elif sx<gx:
                result.append((sy+1,sx+1,sy+1,sx+1+1))
                sx+=1
            elif sx>gx:
                result.append((sy+1,sx+1,sy+1,sx-1+1))
                sx-=1
            else:
                result.append("error2")
    i+=2

print(len(result))
for item in result:
    print(" ".join(map(str,item)))



