SIZE=10**5+1; MOD=10**9+7 #998244353 #ここを変更する
 
SIZE += 1
inv = [0]*SIZE  # inv[j] = j^{-1} mod MOD
fac = [0]*SIZE  # fac[j] = j! mod MOD
finv = [0]*SIZE # finv[j] = (j!)^{-1} mod MOD
inv[1] = 1
fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
for i in range(2,SIZE):
    inv[i] = MOD - (MOD//i)*inv[MOD%i]%MOD
    fac[i] = fac[i-1]*i%MOD
    finv[i]= finv[i-1]*inv[i]%MOD
 
def choose(n,r): # nCk mod MOD の計算
    if 0 <= r <= n:
        return (fac[n]*finv[r]%MOD)*finv[n-r]%MOD
    else:
        return 0
 
def chofuku(ball,box): # nHk mod MOD の計算
    return choose(box+ball-1,box)


N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()

smax=0
smin=0
for i in range(N):
    smax+=A[i]*choose(i,K-1)
    smax%=MOD
    smin+=A[i]*choose(N-i-1,K-1)
    smin%=MOD

print((smax-smin)%MOD)
