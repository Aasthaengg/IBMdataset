P = 10**9+7

fact = [1 for _ in range(2000001)]
inv = [1 for _ in range(2000001)]
fact_inv = [1 for _ in range(2000001)]

for i in range(2, 2000001):
    fact[i] = (fact[i-1]*i) % P
    inv[i] = P - (inv[P % i] * (P // i)) % P
    fact_inv[i] = (fact_inv[i-1] * inv[i]) % P

K = int(input())
S = input()
N = K + len(S)
p = 1
ans = 0
for i in range(K+1):
    ans += p * (fact[N] * fact_inv[N-i] * fact_inv[i] % P)
    ans = ans % P
    p *= 25
    p = p % P

print(ans)