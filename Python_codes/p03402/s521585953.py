a,b=map(int,input().split())
h,w=100,100
la=[]
for i in range(a-1):
    if i==0:
        x,y=0,-2
    else:
        x,y=la[-1]
    y+=2
    if y>=w:
        x+=2
        y=0
    la.append((x,y))
la=set(la)
lb=[]
for i in range(b-1):
    if i==0:
        x,y=51,-2
    else:
        x,y=lb[-1]
    y+=2
    if y>=w:
        x+=2
        y=0
    lb.append((x,y))
lb=set(lb)

ans=[]
print(h,w)
for i in range(100):
    tmp=""
    for j in range(100):
        if (i,j) in la:
            tmp+="."
        elif (i,j) in lb:
            tmp+="#"
        elif i<50:
            tmp+="#"
        else:
            tmp+="."
    print(tmp)





