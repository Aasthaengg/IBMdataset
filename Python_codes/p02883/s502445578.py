n, k = map(int, input().split())
a = sorted(map(int, input().split()))
f = sorted(map(int, input().split()), reverse=True)

lo, hi = -1, 10 ** 18 + 1
while hi - lo > 1:
    mid = (lo + hi) // 2
    if sum(max(0, a[i] - mid // f[i]) for i in range(n)) <= k:
        hi = mid
    else:
        lo = mid

print(hi)
