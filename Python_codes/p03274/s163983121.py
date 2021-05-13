n,k,*a=map(int,open(0).read().split())
ans=10**9
for i in range(n-k+1):
    b,c=a[i],a[i+k-1]
    ans=min(ans,min(abs(b),abs(c))+abs(b-c))
print(ans)