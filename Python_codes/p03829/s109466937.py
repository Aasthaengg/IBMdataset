n,a,b=map(int,input().split())
lst=list(map(int,input().split()))
ans=0
for i in range(1,n):
    d=lst[i]-lst[i-1]
    if d*a<b:
        ans+=d*a
    else:
        ans+=b
print(ans)