N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9+7

combs = [1]*(N-K+1)

for i in range(1,N-K+1):
    combs[i] = (combs[i-1]*(i+K-1)*pow(i,mod-2,mod))%mod

A.sort()
combs = combs[::-1]
ans = 0
for i in range(N-K+1):
    ans += combs[i]*(A[-(i+1)]-A[i])
ans %= mod
print(ans)