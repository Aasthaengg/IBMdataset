x1, y1, x2, y2 = map(int, input().split())

x, y = x2-x1, y2-y1

if x>0 and y>=0:
    x4, y4 = -y, x
elif x<=0 and y>=0:
    x4, y4 = -y, x
elif x<=0 and y<=0:
    x4, y4 = -y, x
elif x>=0 and y<=0:
    x4, y4 = -y, x
x3, y3 = x+x4, y+y4

print(x3+x1, y3+y1, x4+x1, y4+y1)
