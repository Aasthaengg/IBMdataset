n=int(input())
i=1
ans=0
while i*i<=n+1:
    if (n-i)%i==0 and (n-i)//i>i:
        ans+=(n-i)//i
    i+=1
print(ans)