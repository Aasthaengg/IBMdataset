n=int(input())
ans=float('inf')
for i in range(1,n//2+1):
    tmp=0
    a=i
    b=n-i
    while a>0:
        tmp+=a%10
        a//=10
    while b>0:
        tmp+=b%10
        b//=10
    ans=min(ans,tmp)
print(ans)