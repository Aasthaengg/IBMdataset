w,h,x,y = map(int,input().split())

area = (w*h/2)
c = 0

if (x == w/2) and (y == h/2):
    c = 1

print(area,c)