n=int(input())
a=list(map(int,input().split()))
mean=sum(a)/n
dif=abs(mean-a[0])
ans=0
for i in range(n):
    if dif>abs(mean-a[i]):
        dif=abs(mean-a[i])
        ans=i        
print(ans)