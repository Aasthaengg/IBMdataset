x,y=map(int,input().split())
ans=10**10
if x<y:print(min(ans,y-x,abs(x+y)+1))
else:print(min(ans,abs(x+y)+1,abs(x-y)+2))