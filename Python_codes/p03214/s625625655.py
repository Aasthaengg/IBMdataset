n=int(input())
a=list(map(int,input().split()))
x=sum(a)/len(a)
dif=200
for i in range(n):
    if dif>abs(x-a[i]):
        dif=abs(x-a[i])
        ans=i
print(ans)