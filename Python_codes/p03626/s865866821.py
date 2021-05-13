n=int(input())
s=list(input())
t=list(input())
mod=10**9+7
ans=0
if s[0]==t[0]:
    ans=3
else:
    ans=6
for i in range(1,n):
    if s[i]!=s[i-1]:
        if s[i-1]==t[i-1]:
            ans=ans*2%mod
        else:
            if s[i]!=t[i]:
                ans=ans*3%mod
print(ans)    