N, K = map(int, input().split())
ans = 0

for i in range(K+1,N+1):
    ans += (N // i) * (i - K)
    if N >= N // i * i + K:
        ans += N - (N // i * i + K) + 1
    if K == 0:
        ans -= 1

print(ans)