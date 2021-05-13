n,k=map(int,input().split())
x=list(map(int,input().split()))
ans=10**9

for i in range(n-k+1):
    st=x[i]
    ed=x[i+k-1]
    
    if ed<=0:
        ans=min(ans,abs(st))
    elif st>=0 and ed>=0:
        ans=min(ans,ed)
    else:
        t=(min(abs(st),ed)*2)+max(abs(st),ed)
        ans=min(t,ans)

print(ans)
