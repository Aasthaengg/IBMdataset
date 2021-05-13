N,K = map(int, input().split())

mod = 10**9+7

L = [0]*(K+1)
for i in range(K, 0, -1):
    if 2*i > K:
        L[i] = 1
    else:
        for j in range(2, K//i+1):
            L[i] -= L[i*j]
        L[i] += pow(K//i, N, mod)
        L[i] %= mod

ans = 0
for i in range(1, K+1):
    ans += i*L[i]
    ans %= mod
print(ans)