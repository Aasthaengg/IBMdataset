MOD=1000000007
def modpow(a,n,mod):
    res=1
    a=a%mod
    while(n>0):
        if(n&1):
            res=res*a%mod
        a=a*a%mod
        n>>=1
    return res

N=int(input())
A=list(map(int,input().split()))
cnt=[0]*100001
for i in range(N):
    cnt[A[i]]+=1
if(N%2==1):
    if(cnt[0]!=1):
        print(0)
        exit()
    for i in range(2,N,2):
        if(cnt[i]!=2):
            print(0)
            exit()
elif(N%2==0):
    for i in range(1,N,2):
        if(cnt[i]!=2):
            print(0)
            exit()
print(modpow(2,N//2,MOD))