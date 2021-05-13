x1,y1,x2,y2 = map(int,input().split())
vx = x2-x1
vy = y2-y1
print(x2-vy,y2+vx,x2-vy-vx,y2+vx-vy)