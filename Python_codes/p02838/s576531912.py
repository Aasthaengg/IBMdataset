n=int(input())
mod=10**9+7
a=list(map(int,input().split()))
ans=0
for i in range(60):
    ichi=0
    for j in range(n):
        if (a[j]>>i)&1:
            ichi+=1
    zero=n-ichi
    s=ichi*zero*pow(2,i,mod)%mod# xorをしたあとi桁目が1になる組み合わせの個数 x 2**i
    ans+=s
    ans%=mod
print(ans)
