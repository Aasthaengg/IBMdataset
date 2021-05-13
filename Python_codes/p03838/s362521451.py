x,y=map(int,input().split())

ans=0

if abs(x)>abs(y):
    if x<0:
        if y>=0:
            tmp=-x+y
            tmp1=1+-x-y
            ans+=min(tmp,tmp1)
        else:
            ans+=abs(x)-abs(y)
    else:
        ans+=1
        if y>=0:
            tmp=x+y
            tmp1=x-abs(y)+1
            ans+=min(tmp,tmp1)
        else:
            ans+=abs(x)-abs(y)

elif abs(x)==abs(y):
    ans=1

else:
    if x<0:
        if y>=0:
            ans+=1
            ans+=y-abs(x)
        else:
            ans+=2
            ans+=abs(y)-abs(x)
    else:
        if y>=0:
            ans=y-x
        else:
            ans+=1
            ans+=abs(y)-x
print(ans)