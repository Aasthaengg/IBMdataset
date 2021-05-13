def comb(n, r):
    if r<0 or r>n:
        return 0
    r=min(r, n-r)
    return g1[n]*g2[r]*g2[n-r]%MOD

MOD=10**9+7
MAXN=400000+10
g1=[1, 1]
g2=[1, 1]
inverse=[0, 1]

for i in range(2, MAXN+1):
    g1.append((g1[-1]*i)%MOD)
    inverse.append(-inverse[MOD%i]*(MOD//i)%MOD)
    g2.append((g2[-1]*inverse[-1])%MOD)

N, K=map(int, input().split())
if K>=N-1:
    print(comb(N*2-1, N))
else:
    ans=1
    for i in range(1, K+1):
        ans=(ans+(comb(N-1, i)*comb(N, i))%MOD)%MOD
    print(ans)
