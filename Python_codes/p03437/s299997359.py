x,y = map(int,input().split())
if x%y==0:print(-1)
else:print(x*3 if (x*2)%y==0 else x*2)