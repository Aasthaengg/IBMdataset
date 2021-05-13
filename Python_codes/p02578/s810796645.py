n=int(input())
s=list(map(int,input().split()))

ans=0
for i in range(n-1):
    ans+=max(s[i]-s[i+1],0)
    s[i+1]=max(s[i+1],s[i])

print(ans)
