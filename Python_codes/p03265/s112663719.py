x1,y1,x2,y2 = map(int,input().split())

vec12 = (x2-x1, y2-y1)
vec23 = (y1-y2, x2-x1)
vec34 = (x1-x2, y1-y2)

x3,y3 = x2+vec23[0],y2+vec23[1]
x4,y4 = x3+vec34[0], y3+vec34[1]

print(x3, y3, x4, y4)