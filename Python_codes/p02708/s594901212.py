N, K = map(int, input().split())

ans = 0
mod = 10**9+7
for i in range(K, N+2):
    min = i*(i-1)/2
    max = (2*N-i+1)*i/2
    ans += max - min + 1
print(int(ans%mod))