n, m = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
mod = 10**9+7
L = [i*(m-i)%mod for i in range(1, m)]
u = 0
for i in range(m-1):
    u += (Y[i+1] - Y[i]) * L[i] % mod
    u %= mod
M = [i*(n-i)%mod for i in range(1, n)]
ans = 0
for i in range(n-1):
    ans += u * (X[i+1] - X[i]) % mod * M[i] % mod
    ans %= mod
print(ans)
