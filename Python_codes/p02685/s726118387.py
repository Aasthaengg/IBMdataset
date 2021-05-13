n,m,k=map(int,input().split())
mod = 998244353

f= [0]*(n+1)
p= [0]*(n+1)

f[0]=1
p[0]=1
for i in range(1,n+1):
    f[i] = f[i-1]*i%mod
    p[i] = pow(f[i],mod-2,mod)

def nCk(n,k):
    return f[n]*p[k]*p[n-k]%mod

ans = 0
for i in range(k+1):
    if i == 0:
        ans += m*pow(m-1,n-1-i,mod)
    else:
        ans += m*pow(m-1,n-1-i,mod)*nCk(n-1,i)
    ans %= mod
print(ans)

