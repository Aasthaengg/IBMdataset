w,h,x,y = map(int,input().split())
ans = str(w*h/2)
if w==x*2 and h==y*2:
    ans = ans+" 1"
else:
    ans = ans+" 0"
print(ans)