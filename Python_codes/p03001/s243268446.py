w,h,x,y = map(int,input().split())
jud = 0
if 2*x == w and 2*y == h:
    jud = 1
print(w*h/2,jud)