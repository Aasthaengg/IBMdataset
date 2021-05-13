n=int(input())
s=[]
s.append(input())
s.append(input())
mod=10**9+7
state=0
parallel=0
ans=1
for i in range(n):
    if s[0][i]==s[1][i]:
        if i==0:
            ans=3
        else:
            if state==0:
                ans*=2
        state=0
    else:
        if i<2:
            if i==1:
                ans=6
                state=1
        else:
            if parallel==0:
                parallel+=1
            else:
                parallel=0
                if state==0:
                    ans*=2
                else:
                    ans*=3
                state=1
    if ans>mod:
        ans%=mod
print(ans)
