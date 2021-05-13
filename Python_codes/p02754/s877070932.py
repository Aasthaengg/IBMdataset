n,a,b=map(int,input().split())
k=n//(a+b)
mod=n%(a+b)
ans=a*k
if mod >=a:
    ans +=a
else:
    ans +=mod
print(ans)
