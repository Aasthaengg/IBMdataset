w,h,n=map(int,input().split())
mix=0
mx=w
miy=0
my=h
for i in range(n):
    x,y,a=map(int,input().split())
    if a==1:
        mix=max(mix,x)
    elif a==2:
        mx=min(mx,x)
    elif a==3:
        miy=max(miy,y)
    else:
        my=min(my,y)
if mix>=mx or miy>=my:
    print(0)
else:
    print((mx-mix)*(my-miy))
