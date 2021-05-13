w,h,x,y = map(int,input().split())

area = w*h
ans = (w/2==float(x) and h/2==float(y))
print(area/2,(1 if ans else 0))