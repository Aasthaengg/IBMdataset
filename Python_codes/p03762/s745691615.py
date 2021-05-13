N,M = map(int,input().split())
xs = list(map(int,input().split()))
ys = list(map(int,input().split()))
MOD = 10**9+7

total_w = total_h = 0
for n in range(1,N):
    w = xs[n] - xs[n-1]
    w = (w * n * (N-n)) % MOD
    total_w = (total_w + w) % MOD
for n in range(1,M):
    h = ys[n] - ys[n-1]
    h = (h * n * (M-n)) % MOD
    total_h = (total_h + h) % MOD
ans = (total_w * total_h) % MOD
print(ans)
