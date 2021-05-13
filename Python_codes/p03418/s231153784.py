N, K = map(int, input().split())

ans = 0
for a in range(1, N + 1):
    r = N % a
    ans += (N // a) * max(a - K, 0) + min(r, max(0, r + 1 - K))
print(ans)
