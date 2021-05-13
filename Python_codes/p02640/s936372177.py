x,y=map(int,input().split())
if x*4==y or x*2==y:print("Yes")
elif x*2<y<x*4 and (y-(x*2))%2==0 and (4*x-y)%2==0:print("Yes")
else:print("No")