w,h,x,y = map(int,input().split())
tmp1 = abs(w-x)
tmp2 = abs(h-y)

ans = w*h/2

if x == w/2 and y == h/2:
    print(ans,1)
else:
    print(ans,0)