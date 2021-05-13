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
    if(not arr):
        arr.append([1,1])
    if(tmp!=1):
        arr.append([tmp,1])
    return arr
def moddiv(a,m):
    return pow(a,m-2,m)
N=int(input())
A=list(map(int,input().split()))
cnt={}
for i in range(N):
    arr=factorization(A[i])
    for a,b in arr:
        cnt[a]=max(cnt.get(a,0),b)
g=1;res=0
for k,v in cnt.items():
    g=g*(pow(k,v,MOD))%MOD
for i in range(N):
    res=(res+(g*moddiv(A[i],MOD))%MOD)%MOD
print(res)