x,y=map(int,input().split())
print(y-x if x<=y and (0<=x or y<=0) else 2+x-y if y<x and (x<0 or 0<y) else 1+abs(x+y))
