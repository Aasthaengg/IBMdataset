n,k=map(int,input().split())
ans=1
s=(n*(n+1))//2
a=s
b=s
for i in range(n-k+1):
    a-=i
    b-=(n-i)
    ans+=(a-b)+1
    ans=ans%(1000000007)
print(ans)