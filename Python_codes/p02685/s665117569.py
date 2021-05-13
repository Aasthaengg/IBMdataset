N, M, K = map(int, input().split())
mod = 998244353
ans = 0
nCi = [1]

for i in range(1, N+1):
    nCi.append(nCi[i-1]*(N-i) * pow(i, mod-2, mod) % mod)


for i in range(K+1):
    ans += M * pow(M - 1, N-1-i, mod) * nCi[i]
    ans %= mod

print(ans)
