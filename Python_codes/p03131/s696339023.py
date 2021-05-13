k,a,b=map(int,input().split())
ans=0
k+=1
if a+2>b:
    ans=k
else:
    if a+2>k:
        ans=k
    else:
        ans+=b
        k-=a+2
        ans+=(b-a)*(k//2)
        ans+=k%2
print(ans)
