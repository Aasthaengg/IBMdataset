n=int(input())
a=list(map(int,input().split()))
ans=1;before=a[0];mode=0
for i,v in enumerate(a):
    nmode=0
    if before>v:
        nmode=-1
    elif before<v:
        nmode=1
    before=v
    if mode*nmode==-1:
        mode=0
        ans+=1
    elif mode==0:
        mode=nmode
print(ans)