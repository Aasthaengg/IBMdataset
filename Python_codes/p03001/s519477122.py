w,h,x,y = map(int,input().split())
ans1 = 0
ans2 = (h*w) / 2
if w == x*2 and h == y*2:
    ans1 = 1

print(ans2,ans1)