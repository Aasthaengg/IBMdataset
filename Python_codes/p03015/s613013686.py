L=list(input())
mod=10**9+7
N=len(L)
data=[0]*N
data[0]=1
for i in range(1,N):
    data[i]=data[i-1]*3%mod
    
ans=0
num=1
for i in range(N):
    if L[i]=="0":
        continue
    else:
        #直前まで一緒でこの位で０にするとこれ以降自由に選べる
        ans=(ans+num*data[N-1-i])%mod
        num=num*2%mod

ans=(ans+num)%mod
print(ans)