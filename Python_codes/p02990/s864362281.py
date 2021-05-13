n,k=map(int,input().split())
mod=10**9+7
def comb(n,k,mod):
    x = y = 1
    for i in range(min(k,n-k)):
        x = x*(n-i)%mod # 組み合わせの分子
        y = y*(i+1)%mod # 組み合わせの分母
    return x * pow(y, mod-2, mod) % mod
  
for i in range(1,k+1):
  if n-k+1>=i: # 赤のボールが青のボールを置く場所以上にある場合
    
    print((comb(n-k+1,i,mod)*comb(k-1,i-1,mod))%mod)
  else:
    print(0)