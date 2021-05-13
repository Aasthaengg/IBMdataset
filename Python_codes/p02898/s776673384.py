from bisect import bisect_left
N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
res = 0
idx = bisect_left(H, K)
if idx < N:
    if H[idx] < K:
        res = N - idx - 1
    else:
        res = N - idx
print(res)

