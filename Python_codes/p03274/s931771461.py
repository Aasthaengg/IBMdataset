n,k=map(int,input().split())
x=list(map(int,input().split()))
ans=10**25
for i in range(n-k+1):
    if x[i+k-1]<=0:
        num=x[i]*-1
    elif x[i]>=0:
        num=x[i+k-1]
    else:
        num1=abs(x[i])
        num=min(num1,x[i+k-1])*2+max(num1,x[i+k-1])
    ans=min(ans,num)
print(ans)
