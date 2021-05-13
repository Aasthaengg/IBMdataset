n,k=map(int,input().split())
a=list(map(int,input().split()))
x,ans=0,0
for i in range(40,-1,-1):
    cnt1=0
    for j in a:
        if j>>i&1:
            cnt1+=1
    if n-cnt1>cnt1 and x+2**i<=k:
        x+=2**i
        ans+=(n-cnt1)*2**i
    else:
        ans+=cnt1*2**i
print(ans)