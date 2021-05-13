s=int(input())
x3,y3,x2,y2,y1=0,0,-int(-s**0.5//1),1,-int(-s**0.5//1)
x1=x2*y1-s
if x2*y1-s==0:
    x1,y2=0,0
print(x1,y1,x2,y2,x3,y3)