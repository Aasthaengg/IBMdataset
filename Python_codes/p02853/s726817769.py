x,y=map(int,input().split())
l=[0,300000,200000,100000]
if x==y==1:
 print(l[x]+l[y]+400000)
else:
    if y > 3:
        y=0
    if x>3:
        x=0
    print(l[x]+l[y])