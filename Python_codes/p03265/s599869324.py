x1,y1,x2,y2 = map(int,input().split())

dx = x2 - x1
dy = y2 - y1

nx1 = -dy
ny1 = dx
nx2 = -ny1
ny2 = nx1

print(x2+nx1,y2+ny1,x2+nx1+nx2,y2+ny1+ny2)