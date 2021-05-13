s=list(input())
n=len(s)
ans=1
for i in range(n-1):
    if s[i]!=s[i+1]:
        ans+=1
print(ans-1)
