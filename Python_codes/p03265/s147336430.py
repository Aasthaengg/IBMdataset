x1,y1,x2,y2 = [int(i) for i in input().split()]

height = y2 - y1
width = x2 - x1

x3 = x2 - height
x4 = x3 - width
y3 = y2 + width
y4 = y3 - height

print(x3,y3,x4,y4)