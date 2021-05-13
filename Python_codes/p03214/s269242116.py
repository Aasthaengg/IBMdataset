n=int(input())
a=list(map(int,input().split()))
ave=sum(a)/n
ans=0
dif=100
for i in range(n):
    tmp=abs(ave-a[i])
    if tmp<dif:
        ans=i
        dif=tmp
print(ans)