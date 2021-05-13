N=int(input())
ans=1
i=1
while i<=N:
    ans=(ans*i)%(10**9+7)
    i+=1
print(ans)