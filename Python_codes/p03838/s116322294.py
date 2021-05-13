x,y=map(int,input().split())
ans=0
if x>=0 and y>=0 and y>=x:
    print(y-x)
elif x>=0 and y>0 and y<x:
    x*=-1
    ans=+1#xを負にする
    ans+=abs(x)-y
    ans+=1#xを正に戻す
    print(ans)
elif x>0 and y==0:
    print(x+1)
elif x>y and x>0 and y<0:
    if abs(x)>=abs(y):
        x*=-1
        ans=+1#xを負にする
        ans+=abs(x)-abs(y)
        print(ans)
    elif abs(x)<abs(y):
        ans+=abs(y)-abs(x)
        ans+=1#xを負にする
        print(ans)
elif x==0 and y<0:
    print(-y+1)
elif x<0 and y>0:
    if abs(x)>=abs(y):
        ans+=abs(x)-abs(y)
        ans+=1#xを正にする
        print(ans)
    elif abs(x)<abs(y):
        x*=-1
        ans+=1#xを正にする
        ans+=(y-x)
        print(ans)
elif x<0 and y==0:
    print(y-x)
elif x<0 and y<0:
    if x<=y:
        print(y-x)
    elif x>y:
        x*=-1#xを正にする
        ans+=1
        ans+=abs(y)-abs(x)
        ans+=1#xを負に戻す
        print(ans)