x1,y1,x2,y2 = map(int,input().split())
a = x2+(y1-y2)
b = y2-(x1-x2)
print(a,b,a+(x1-x2),b+(y1-y2))