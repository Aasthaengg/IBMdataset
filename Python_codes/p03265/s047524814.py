x1, y1, x2, y2 = list(map(int, input().split())) 

#solve x4y4
x2da = x2 - x1
y2da = y2 - y1

x4da = -y2da  
y4da = x2da

x4 = x4da + x1
y4 = y4da + y1

#solve x3y3
x1da = x1 - x2
y1da = y1 - y2

x3da = y1da
y3da = -x1da

x3 = x3da + x2
y3 = y3da + y2

print(x3, end=" ")
print(y3, end=" ")
print(x4, end=" ")
print(y4)