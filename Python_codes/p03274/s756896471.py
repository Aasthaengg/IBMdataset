n,k=map(int,input().split())
x=list(map(int,input().split()))

ans=float('inf')
for i in range(n-k+1):
    nowx=(x[i],x[i+k-1])
    if nowx[0]>=0 and nowx[-1]>=0:
        ans=min(ans, nowx[-1])
    elif nowx[0]<=0 and nowx[-1]<=0:
        ans=min(ans, abs(nowx[0]))
    elif nowx[0]<0 and nowx[-1]>=0:
        ans=min(ans, 2*abs(nowx[0])+nowx[-1], abs(nowx[0])+2*nowx[-1])
print(ans)