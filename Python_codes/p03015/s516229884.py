S=input()
L=[0]*len(S)
for i in range(len(S)):
    L[i]=int(S[i])

mod=10**9+7    
    
N=len(S)
power=[1]*(N+3)
for i in range(1,N+3):
    power[i]=(power[i-1]*3)%mod

    

ans=1
for i in range(N):
    if L[N-1-i]==1:
        ans=(2*ans+power[i])%mod
print(ans%mod)