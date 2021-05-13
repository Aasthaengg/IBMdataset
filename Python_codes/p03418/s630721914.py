N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    ans += N // i * max(0, i - K) + max(0, N % i - K + 1)

print(ans if K > 0 else ans - N)
