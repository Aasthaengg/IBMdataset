N, x = map(int, input().split())
*A, = map(int, input().split())
ans = 0
for i in range(N - 1):
    w = A[i] + A[i + 1]
    if w <= x: continue
    r = max(0, A[i + 1] - (w - x))
    l = x - r
    ans += A[i] - l + A[i + 1] - r
    A[i + 1] = r
print(ans)
