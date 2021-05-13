k,a,b=map(int, input().split())

ans=0

if a+1>=b or k<=a:
    ans=k+1
else:
    k-=(a-1)
    ans=a
    exchange=k//2
    ans+=(b-a)*exchange

    k-=2*exchange
    ans+=k

print(ans)