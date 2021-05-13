a,b=sorted(map(int,input().split()))
mod=10**9+7
ans=1
if a==b:
    for i in range(1,a+1):
            ans=ans*i*i%mod
    ans=ans*2%mod        
elif b-a>1:ans=0
else:
    for i in range(1,a+1):
        ans=ans*i*i%mod
    ans=ans*b%mod
print(ans)