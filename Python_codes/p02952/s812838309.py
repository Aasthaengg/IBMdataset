n=int(input())

ans=0
i=1

while i<=n:

    if len(str(i))%2==1:
        ans+=1

    i+=1

print(ans)