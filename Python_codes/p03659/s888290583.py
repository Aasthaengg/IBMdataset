N=int(input())
a=list(map(int,input().split()))

X=sum(a)
tmp=a[0]
ans=abs(X-2*tmp)
for i in range(1,N-1):
    tmp+=a[i]
    ans=min(ans,abs(X-2*tmp))
print(ans)