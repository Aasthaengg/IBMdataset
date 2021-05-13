N,M = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))

MOD = 10**9+7
w_sum = 0
for i in range(N//2):
    times = N-1 - i*2
    w = X[-1-i] - X[i]
    w_sum += (w*times)%MOD
    w_sum %= MOD

h_sum = 0
for i in range(M//2):
    times = M-1 - i*2
    h = Y[-1-i] - Y[i]
    h_sum += (h*times)%MOD
    h_sum %= MOD

print((w_sum * h_sum) % MOD)