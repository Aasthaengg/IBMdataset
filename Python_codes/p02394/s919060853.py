w,h,x,y,r=map(int,input().split())
if r<=x<=w-r:
  if r<=y<=h-r:print("Yes");exit()
print("No")
