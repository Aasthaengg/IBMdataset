N, K = map(int, input().split())

ans = 0
for b in range(1, N+1):
    d, m = divmod(N+1, b)
    k = max(b-K, 0)
    ans += max(k*d, 0)
    if K == 0:
        ans -= 1
    ans += max(m-K, 0)

print(ans)