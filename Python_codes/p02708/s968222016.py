N, K = map(int, input().split())
MOD = 10**9+7
cnt = 1
for k in range(K, N+1):
    cnt += (N+N-k+1)*k//2-(0+k-1)*k//2+1
    cnt %= MOD
print(cnt)