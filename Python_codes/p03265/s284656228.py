MM = input().split()
x1 = int(MM[0])
y1 = int(MM[1])
x2 = int(MM[2])
y2 = int(MM[3])
a = x2 - x1
b = y2 - y1
x3 = x2 - b
y3 = y2 +a
x4 = x1 -b
y4 = y1 + a
print(x3,y3,x4,y4)