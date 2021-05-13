n=int(input())
ans=10**6
for i in range(1,n+1):
    a=i
    b=n-i
    if a<=b:
        asum=sum(map(int,str(a)))
        bsum=sum(map(int,str(b)))
        if ans>(asum+bsum):
            ans=asum+bsum
print(ans)