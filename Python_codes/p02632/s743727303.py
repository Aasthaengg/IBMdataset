mod=10**9+7
k=int(input())
s=input()
n=len(s)
ans=0
r=pow(26,k,mod)
c=1
for i in range(k+1):
    ans+=r*c
    ans%=mod
    r*=25*pow(26,mod-2,mod)
    r%=mod
    c*=(n+i)*pow(i+1,mod-2,mod)
    c%=mod
print(ans)
