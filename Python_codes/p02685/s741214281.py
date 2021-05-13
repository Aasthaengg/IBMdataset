mod = 998244353
n,m,k = map(int, input().split())
def setFact(n, mod):
    global fact
    global ifact
    fact = [0]*(n+1)
    fact[0] = 1
    ifact = [0] * (n+1)
    for i in range(1, n+1):
        fact[i] = (fact[i-1]*i)%mod
    ifact[n] = pow(fact[n], mod-2, mod)
    for i in range(1, n+1):
        ifact[n-i] = ifact[n-i+1]*(n-i+1)%mod
def combination(n, k, mod):
    global fact
    global ifact
    if k < 0 or k > n:
        return 0
    else:
        return fact[n]*ifact[n-k]*ifact[k]%mod
setFact(n, mod)
ans = 0
now = pow(m-1, n-1-k, mod)
for i in range(k, -1, -1):
    ans = (ans + m*now*combination(n-1, i, mod)) %mod
    now *= m-1
    now %= mod
print(ans)