#!/usr/bin/python3

M = 998244353

def facts(n, MOD):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
     
    return factorials, invs


(n, m, k) = map(int, input().split())

(fcs, invs) = facts(n, M)

c = 0
for i in range(k + 1):
    c = (c + m * fcs[n - 1] * invs[i] * invs[n - 1 - i] * pow(m - 1, n - 1 - i, M)) % M

print(c)

    
