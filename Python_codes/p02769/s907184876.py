n, k = map(int, input().split())

mod = 10 ** 9 + 7

fact = [1]
fact_inv = [0] * (n+1)
for i in range(n):
    fact.append(fact[-1] * (i+1) % mod)
fact_inv[-1] = pow(fact[-1], mod-2, mod)
for i in range(n-1, -1, -1):
    fact_inv[i] = fact_inv[i+1] * (i+1) % mod

ans = 0
for i in range(min(n-1, k) + 1):
    com1 = fact[n] * fact_inv[i] * fact_inv[n-i] % mod
    com2 = fact[n-1] * fact_inv[i] * fact_inv[n-i-1] % mod
    mul = com1 * com2 % mod
    ans = (ans + mul) % mod

print(ans)