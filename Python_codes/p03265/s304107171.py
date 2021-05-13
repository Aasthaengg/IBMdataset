#B - Ruined Square
x1,y1,x2,y2 = map(int,input().split())

y3 = y2 + (x2-x1)
x3 = x2 - (y2-y1)
y4 = y1 + (x2-x1)
x4 = x1 - (y2-y1)
A = [x3,y3,x4,y4]
print(*A)