N ,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
MOD = 10**9+7

def combinations_count(n, r):
    if n >= r:
        return ((fact[n] * fact_inv[n-r])%MOD) * fact_inv[r]%MOD
    else:
        return 0

fact = [1] * (N+1)
fact_inv = [1] *(N+1)
for i in range(1,N+1):
    fact[i] = (fact[i-1] * i)%MOD
    fact_inv[i] = pow(fact[i],MOD-2,MOD)

ans = 0
L = len(A)
for i,a in enumerate(A):
    MIN = combinations_count(L-1-i,K-1)
    MAX = combinations_count(i,K-1)
    ans += MAX*a - MIN*a
    ans %= MOD

print(ans)