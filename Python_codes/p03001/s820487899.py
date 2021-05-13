w,h,x,y = map(int,input().split())

total = w*h
ans = total/2
route = 0
if w == x*2 and h == y*2:
    route = 1

print(ans, route)

