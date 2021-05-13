n=input()
ans=0
x=-1
n=n+str(0)
for i in range(len(n)-1):
    v=int(n[i])
    w=int(n[i+1])
    if x<0:
        if v<5:
            ans+=v
        elif v==5:
            if w>=5:
                ans+=9-v+2
                x+=1
            else:
                ans+=v
        else:
            ans+=9-v+2
            x+=1
    else:
        if v<4:
            ans+=v
            x-=1
        elif v==4:
            if w>=5:
                ans+=9-v
            else:
                ans+=v
                x-=1
        else:
            ans+=9-v

print(ans)