N, K = map(int, input().split())
ans = -N+K if K == 0 else 0
for b in range(K+1, N+1):
    ans += N // b * (b - K) + max(0, N - N // b * b - K + 1)
print(ans)