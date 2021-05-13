x1,y1,x2,y2=map(int,input().split())

vec12_x=-(y2-y1)
vec12_y=x2-x1

x3=x2+vec12_x
y3=y2+vec12_y

x4=x3-(x2-x1)
y4=y3-(y2-y1)

print(x3,y3,x4,y4)