N, K = map(int, input().split())
ans = 0
for b in range(K+1, N+1):
    H = N // b
    n = b - K
    Last = N % b
    ans += H * n + max(Last - K + 1, 0)
    if K == 0:
        ans -= 1
print(ans)