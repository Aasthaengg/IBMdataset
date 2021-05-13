N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)

hi = 10**18
lo = -1

while hi - lo > 1:
    mid = (hi + lo) // 2
    tr = 0
    for i in range(N):
        if A[i] * F[i] > mid:
            tr += A[i] - mid // F[i]
    if tr > K:
        lo = mid
    else:
        hi = mid

print(hi)