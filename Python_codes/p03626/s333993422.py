n=int(input())
s=[input() for i in range(2)]
mod=10**9+7

if s[0][0]==s[1][0]:
    ans=3
    i=1
    tate=True
else:
    ans=6
    i=2
    tate=False

while i<n:
    if s[0][i]==s[1][i]:
        if tate==True:
            ans*=2
        else:
            pass
        tate=True
        i+=1
    else:
        if tate==True:
            ans*=2
        else:
            ans*=3
        i+=2
        tate=False
    
    ans=ans%mod
print(ans)