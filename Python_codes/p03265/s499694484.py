x1, y1, x2, y2 = map(int, input().split())
X2=x2-x1
Y2=y2-y1
x3=X2-Y2+x1
y3=X2+Y2+y1
x4=-Y2+x1
y4=X2+y1
print(x3, y3, x4, y4)