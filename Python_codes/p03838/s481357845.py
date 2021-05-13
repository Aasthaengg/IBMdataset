x,y=map(int,input().split())

ans=0
if x*y>0:
    if x<=y:
        ans=abs(y-x)
    else:
        ans=2+abs(y-x)
elif x*y<0:
    ans=1+abs(y+x)
else:
    if x<=y:
        ans=abs(y-x)
    else:
        ans=1+abs(y-x)
print(ans)