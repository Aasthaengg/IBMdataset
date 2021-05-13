n=int(input())

ans=0
if n%2==0:
    n=n//2
    i=1
    while 5**i<=n:
        ans+=n//(5**i)
        i+=1
print(ans)