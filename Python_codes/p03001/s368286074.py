w,h,x,y=map(int,input().split())
ans=[0,0]
ans[0]=w*h/2.0
ans[1]=1 if (x*2==w and y*2==h) else 0
print(*ans,sep=" ")