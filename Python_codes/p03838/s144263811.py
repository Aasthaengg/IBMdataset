x,y=map(int,input().split())
if 0<=x<y or x<y<=0:
    print(y-x)
elif 0<y<x or y<x<0:
    print(2+x-y)
elif x<0<y or y<0<x:
    print(1+abs(x+y))

if x==0 and y<0 :
    print(abs(y)+1)
if y==0 and x>0:
    print(x+1)