n=int(input())
s1=input()
s2=input()
mod=1000000007
t=0
flg=True
ans=1
while t<n:
    if t==0:
        if s1[t]==s2[t]:
            t+=1
            ans*=3
        else:
            t+=2
            ans*=6
            flg=False
    elif flg and s1[t]==s2[t]:
        ans*=2
        ans%=mod
        t+=1
    elif flg and s1[t]!=s2[t]:
        t+=2
        ans*=2
        ans%=mod
        flg=False
    elif flg==False and s1[t]==s2[t]:
        flg=True
        t+=1
    elif flg==False and s1[t]!=s2[t]:
        t+=2
        ans*=3
        ans%=mod
print(ans%mod)