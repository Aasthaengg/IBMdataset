x,y=map(int,input().split())
ans=10**9+100
for i in range(1<<2):
    if (i>>0)&1:
        x1=x*-1
    else:
        x1=x
    if (i>>1)&1:
        y1=y*-1
    else:
        y1=y
    if x1<=y1:
        ans=min(ans,y1-x1+((i>>0)&1)+((i>>1)&1))

print(ans)