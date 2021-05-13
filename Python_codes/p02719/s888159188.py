n, k = map(int, input().split())

ans = n
if abs(n-k) > k:
    x = abs(n-k)//k
    n = abs(n-k) - x*k
ans = min(ans, n, abs(n-k), abs(abs(n-k)-k))
print(ans)