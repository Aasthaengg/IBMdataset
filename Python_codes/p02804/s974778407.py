N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

MOD = 10 ** 9 + 7

def factorial(n):
    global fct
    global invfct
    fct = [0] * (n + 1)
    fct[0] = 1
    for i in range(1, n+1):
        fct[i] = fct[i-1] * i % MOD
    invfct = [0] * (n + 1)
    invfct[n] = pow(fct[n], MOD - 2, MOD)
    for i in range(n-1, -1, -1):
        invfct[i] = invfct[i+1] * (i + 1) % MOD

factorial(N)

def binomial(n, k):
    return fct[n] * invfct[n-k] % MOD * invfct[k] % MOD

answer = 0

for i in range(N):
    if N - i - 1 < K - 1:
        break
    answer -= A[i] * binomial(N-i-1, K-1) % MOD
    answer %= MOD

for i in range(N-1, -1, -1):
    if i < K - 1:
        break
    answer += A[i] * binomial(i, K-1) % MOD
    answer %= MOD

print(answer)
