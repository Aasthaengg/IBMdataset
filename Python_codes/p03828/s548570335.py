MOD = 10 ** 9 + 7

n = int(input())

S = [0] * (n+1)

for i in range(1, n+1):
    n_i = i
    p = 2 
    while n_i > 1:
        while n_i % p == 0:
            n_i //= p
            S[p] += 1
        p += 1

ans = 1
for s in S:
    ans *= s+1

print(ans % MOD)