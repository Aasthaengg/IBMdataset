def nPr(n,r,mod):
    if r==0: return 1
    if r==1: return n
    ans=1
    for i in range(r):
        ans=(n-i)*ans%mod
    return ans%mod
    
n,m=map(int,input().split())

mod=10**9+7
dog=nPr(n,n,mod)
mon=nPr(m,m,mod)

if abs(n-m)>1:
    print(0)
elif abs(n-m)==1:
    print(dog*mon%mod)
else:
    print(dog*mon*2%mod)