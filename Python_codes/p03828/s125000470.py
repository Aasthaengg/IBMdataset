# coding: utf-8

#素因数分解
def prime_factorize(N):
    f = []
    while N % 2 == 0:
        f.append(2)
        N //= 2
    i = 3
    while i * i <= N:
        while N % i == 0:
            f.append(i)
            N //= i
        i += 2
    #最後残った数について
    if N != 1:
        f.append(N)
    return f

#main
N = int(input())
MOD = 10**9 + 7
exp = [0] * (N+1)

for i in range(2, N+1):
    F = prime_factorize(i)
    for j in range(len(F)):
        exp[F[j]] += 1

ans = 1
for i in range(N+1):
    ans *= exp[i] + 1
    ans %= MOD
print(ans)