n,l=map(int, input().split())

taste=[l+i-1 for i in range(1,n+1)]
dif=10**10
for i in taste:
    if dif>abs(i):
        ans=sum(taste)-i
        dif=abs(i)
print(ans)