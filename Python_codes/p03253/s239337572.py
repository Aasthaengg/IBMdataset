MOD=10**9+7
def factorization(n):
    arr=[]
    tmp=n
    for i in range(2,int(n**0.5)+1):
        if(tmp%i==0):
            cnt=0
            while tmp%i==0:
                cnt+=1
                tmp//=i
            arr.append([i,cnt])
    if(tmp!=1):
        arr.append([tmp,1])
    return arr
def com(n,k,mod):
    res=1
    tmp=1
    for i in range(1,k+1):
        res=res*(n-i+1)%mod
        tmp=tmp*i%mod
    a=pow(tmp,mod-2,mod)
    return res*a%mod
N,M=map(int,input().split())
a=1
arr=factorization(M)
for x,y in arr:
    a=(a*com(y+N-1,N-1,MOD))%MOD
print(a)