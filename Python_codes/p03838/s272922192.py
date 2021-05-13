x,y=map(int,input().split())
res = 0
if 0<=x<=y:
    res = y-x
elif 0<y<x:
    res = x-y+2
elif y==0 and x>0:
    res = x+1
elif y==0 and x<0:
    res = abs(x)
elif x==0 and y>0:
    res = y
elif x==0 and y<0:
    res = abs(y)+1
elif x<0<y:
    res = abs(x+y)+1
elif y<0<x:
    res = abs(x+y)+1
elif x<=y<=0:
    res = y-x
elif y<x<=0:
    res = x-y+2
print(res)
