import sys
input = sys.stdin.readline
mod = 10 ** 9 + 7
N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
minus = 0
plus = 0
fact = [0] * (N+1)
fact[0] = 1
pow_fact = [0] * (N+1)
pow_fact[0] = 1
fa = 1
for i in range(1, N+1):
    fa *= i
    fa %= mod
    fact[i] = fa
    pow_fact[i] = pow(fa, mod-2, mod)
b = pow_fact[K-1]
for i in range(N-K+1):
    a = fact[N-i-1]
    c = pow_fact[N-i-K]
    comb = (a*b*c) % mod
    minus += (A[i] * comb) % mod
    plus += (A[-i-1] * comb) % mod
print((plus - minus) % mod)