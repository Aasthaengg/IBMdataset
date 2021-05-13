n,m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
res = 0
mod = 10**9+7
for i in range(n):
    res += (i*x[i])%mod-(n-i-1)*x[i]%mod
    res %= mod
ans = 0
for i in range(m):
    ans += ((i)*y[i])%mod-((m-i-1)*y[i])%mod
    ans %= mod
ans *=res
ans %=mod
print(ans)
