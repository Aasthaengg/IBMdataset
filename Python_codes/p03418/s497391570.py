import math 
n,k=map(int,input().split())
if k==0:
    print(n**2)
if k>=1:
    ans=0
    flow=0
    for some in range(k+1,n+1):
        flow=math.floor(n/some)*(some-k)
        ans+=flow
        if  math.floor(n/some)*some+k>n:
            ans=ans
        if math.floor(n/some)*some+k<=n:
            ans=ans+n+1-math.floor(n/some)*some-k

    print(ans)