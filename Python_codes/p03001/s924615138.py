w,h,x,y = map(int,input().split())

ans2=0
if (x==w/2 and y==h/2):
    ans2=1
print(w*h/2,ans2)
