x,y=map(int,input().split())

if x*y<0:
    ans=abs(abs(y)-abs(x))+1
elif x==0:
    ans=abs(y)
    if y<0:
        ans+=1
elif y==0:
    ans=abs(x)
    if x>0:
        ans+=1
else:
    ans=abs(abs(y)-abs(x))
    if x>y:
        ans+=2

print(ans)