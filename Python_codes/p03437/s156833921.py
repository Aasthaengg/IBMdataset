x,y=map(int,input().split())
ans=x*y-x
if ans%y==0:
    print(-1)
else:
    print(ans)