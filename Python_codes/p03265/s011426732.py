a,b,c,d= map(int, input().split())
x = c - a
y = d - b
x3 = c- y
y3 = d+ x
x4 = a- y
y4 = b+ x
print(x3,y3,x4,y4)