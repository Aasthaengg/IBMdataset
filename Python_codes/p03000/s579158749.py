n,x=map(int,input().split())
a=list(map(int,input().split()))
sum=0
ans=1
for i in range(n) :
    sum+=a[i]
    if sum <= x :
        ans+=1
print(ans)