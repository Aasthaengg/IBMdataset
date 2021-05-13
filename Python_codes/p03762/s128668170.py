N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
mod = 10**9+7
x = 0
y = 0
for i in range(N):
    x += (-N+1+2*i)*X[i]
    x %= mod
for i in range(M):
    y += (-M+1+2*i)*Y[i]
    y %= mod
print(x*y % mod)
