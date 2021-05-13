w,h, x,y = map(int,input().split())
ans = w*h/2
if w%2==0 and h%2==0:
    if w//2==x and h//2==y:
        print(ans, 1)
    else:
        print(ans, 0)
else:
    print(ans, 0)