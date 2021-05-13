x1,y1,x2,y2=map(int,input().split())
x3=x2+(y1-y2)
y3=y2-(x1-x2)
x4=x3+(x1-x2)
y4=y3+(y1-y2)
Z=[str(x3),str(y3),str(x4),str(y4)]
print(' '.join(Z))