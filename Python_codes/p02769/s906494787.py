n, k = map(int, input().split())
mod = 10**9 + 7
def setFact(n, mod):
    global fact
    fact = [1]
    global ifact
    ifact = [1] * (n+1)
    for i in range(1, n+1):
        fact.append(fact[i-1]*i%mod)
    ifact[-1] = pow(fact[-1], mod-2, mod)
    for i in range(2, n+2):
        ifact[-i] = ifact[-i+1]*(n-i+2) %mod
def combination(n, k , mod):
    global fact
    global ifact
    if k < 0 or k > n:
        return 0
    else:
        return fact[n] * ifact[n-k] * ifact[k] % mod
setFact(n, mod)
ans = 0
for i in range(min(n+1, k+1)):
    ans += combination(n,i,mod) *combination(n-1,i, mod) %mod
    ans %= mod
print(ans)