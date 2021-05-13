def pow(a,b):
    ans=1
    if b==0:
        return 1
    for i in range(b):
        ans=ans*a
        if ans > mod:
            ans=ans%mod
    return ans%mod
        
        
mod=1000000007

n=int(input())

if n==1:
    print(0)
else:
    ans=pow(10,n)+pow(8,n)-(pow(9,n)*2)
    print(ans%mod)
