n,k=map(int,input().split())
if k==0:
    print(n**2)
    exit()
ans=0
for i in range(k+1,n+1):
    ans+=(n//i)*(i-k)
    if n%i>=k:
        ans+=(n%i)-k+1
print(ans)