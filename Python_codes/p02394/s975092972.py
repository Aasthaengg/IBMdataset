w,h,x,y,r=map(int,input().split())
if 0>x-r or w<x+r:
    print("No")
elif 0>y-r or h<y+r:
    print("No")
else:
    print("Yes")