n,m=map(int,input().split())
p=10**9+7
n,m=min(n,m),max(n,m)
if m-n>=2:
    print(0)
elif m-n==1:
    ans=1
    for i in range(m):
        ans=ans*(i+1)%p
    for i in range(n):
        ans=ans*(i+1)%p
    print(ans%p)
else:
    ans=1
    for i in range(n):
        ans=ans*(i+1)%p
    print(2*ans*ans%p)

