N,K = map(int,input().split())
b = K
r = N-K
mod = 10**9+7
# rのしきりr+1にi個いれる→(r+1)Ci
# bはしきりb-1にi-1個入れる→(b-1)C(i-1)

ans = (r+1)
print(ans)
for i in range(2,K+1):
    ans *= (r+1)-(i-1)
    ans *= (b-1)-(i-2)
    ans *= pow(i,mod-2,mod)
    ans *= pow(i-1,mod-2,mod)
    ans %= mod
    print(ans)