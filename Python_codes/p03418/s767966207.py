n, k=map(int, input().split())

if k==0:
    ans=n**2
else:
    ans=0
    for i in range(k+1, n+1):
        div=n//i
        mod=n%i
        ans+=div*(i-k)
        ans+=max(0, mod-k+1)
print(ans)