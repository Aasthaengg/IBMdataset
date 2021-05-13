n,k=map(int,input().split())
x=list(map(int,input().split()))
ans=float("inf")
for i in range(n-k+1):
    sm=x[i]
    sp=x[i+k-1]
    if sp<0:
        ans=min(-sm,ans)
    elif 0<sm:
        ans=min(ans,sp)
    else:
        ans=min(ans,min(sm*-2+sp,sp*2-sm))
print(ans)