import sys
input=sys.stdin.readline
x1,y1,x2,y2=map(int,input().split())
d=(x2-x1,y2-y1)
d=(-d[1],d[0])
x3=x2+d[0]
y3=y2+d[1]
d=(-d[1],d[0])
x4=x3+d[0]
y4=y3+d[1]
print(x3,y3,x4,y4)





