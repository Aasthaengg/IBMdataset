MOD = 10**9 + 7

def prepare(n, MOD):
 
    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
     
    return factorials, invs


k = int(input())
s = input()
n = len(s)
ans = 0

l = k+n + 3
 
a25 = [1]
for i in range(l):
    a25.append((a25[-1] * 25) % MOD)
a26 = [1]
for i in range(l):
    a26.append((a26[-1] * 26) % MOD)

fact, inv = prepare(n+k, MOD)
for i in range(k+1):
    c25 = a25[i]
    f = fact[i+n-1] * inv[i] % MOD * inv[n-1] % MOD
    c25 *= f
    c25 %= MOD

    c26 = a26[k-i]
    ans += (c25 * c26 % MOD)
    ans %= MOD
print(ans)
