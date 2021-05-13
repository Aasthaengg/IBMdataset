k = int(input())
s = input()

def pre(n,MOD):
    f = 1
    factor = [1]
    for m in range(1,n+1):
        f *= m
        f %= MOD
        factor.append(f)
    inv = pow(f,MOD-2,MOD)
    invs = [1] * (n+1)
    for m in range(n,1,-1):
        inv *= m
        inv %= MOD
        invs[m-1] = inv
    return factor,invs

MOD = 10**9 + 7
n = len(s)
factor,invs = pre(n+k,MOD)
ans = 0
for i in range(k+1):
    temp = 1
    temp = (temp * factor[n-1+k-i] * invs[n-1] * invs[k-i]) % MOD
    temp = temp * pow(25,k-i,MOD) % MOD
    temp = temp * pow(26,i,MOD) % MOD
    ans = (ans + temp) % MOD
print(ans)