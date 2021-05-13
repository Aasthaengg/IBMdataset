mod=10**9+7

L=input()
l=len(L)
ans=3**(l-1)
a=L.count('1')
cnt=1

for i in range(1,l):
    if L[i]=='1':
        ans+=pow(2,cnt,mod)*pow(3,l-i-1,mod)
        cnt+=1
        
print((ans+pow(2,a,mod))%mod)