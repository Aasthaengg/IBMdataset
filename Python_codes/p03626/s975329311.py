n=int(input())
mod=10**9+7
ans=1
pre=0
s,t=input()+"#",input()+"#"
now=0
yoko=[6,2,3]
tate=[3,2,1]
while now<n:
    if s[now]==s[now+1]:
        ans=ans*yoko[pre]%mod
        pre=2
        now+=2
    else:
        ans=ans*tate[pre]%mod
        pre=1
        now+=1
print(ans)