N, K = map(int, input().split())
MOD = 10**9+7
A = [a % MOD for a in sorted(list(map(int, input().split())))]
MIN, MAX = 0, 0

def div_MOD(a):     # (a^{-1} mod MOD) をフェルマーの小定理より求める
    return pow(a, MOD - 2, MOD)     # a^{-1} = a^{p-2} (mod p)

C = [0]*(K-1) + [1]
for n in range(K, N):
    C.append((C[n-1] * n * div_MOD(n-(K-1))) % MOD)

for i in range(N-K+1):
    MIN = (MIN + (A[i] * C[N-i-1]) % MOD) %MOD
for i in range(N-K+1):
    MAX = (MAX + (A[N-1-i] * C[N-i-1]) % MOD) %MOD

print((MAX - MIN) % MOD)