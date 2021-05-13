n,a,b=map(int,input().split())
ans=0
for i in range(1,n+1):
    s=str(i)
    sum=0
    for j in range(len(s)):
        sum+=int(s[j])
    if a<=sum and sum<=b:
        ans+=i
print(ans)

