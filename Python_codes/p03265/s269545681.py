x1,y1,x2,y2 = map(int,input().split())
if x1 == x2:
    print(x2+(y1-y2), y2, x2+(y1-y2), y1)
elif y1 == y2:
    print(x2, y2+(x2-x1), x1, y2+(x2-x1))
else:
    print(x2-(y2-y1), y2+(x2-x1), x1-(y2-y1), y1+(x2-x1))
