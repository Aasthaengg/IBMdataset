x,y=map(int,input().split())

if y<0<x or x<0<y:
    print(abs(abs(y)-abs(x))+1)
elif x<y and x!=0:
    print(y-x)
elif y<x and x!=0 and y!=0:
    print(x-y+2)
elif x<y and x==0:
    print(y-x)
elif y<x and x==0 or y==0:
    print(x-y+1)
