x,y=map(int,input().split())
#print(y-x,x-y+2,1+y+x,(-y-x)+1,y+x+1)

l=[]

if x<0:
    if y<x:
        print(x-y+2)
    elif y<=0:#x<=y<=0
        print(y-x)
    else:
        print(max(abs(x),abs(y))-min(abs(x),abs(y))+1)

elif x==0:
    if y<x:
        print(x-y+1)
    else:
        print(y-x)
else:#x>0
    if y>=x:
        print(y-x)
    elif x>y>0:
        print(x-y+2)
    elif y==0:
        print(x-y+1)
    else:
        print(max(abs(x),abs(y))-min(abs(x),abs(y))+1)
