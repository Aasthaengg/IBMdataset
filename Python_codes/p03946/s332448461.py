N, T = map(int, input().split())
A = list(map(int, input().split()))

lo = 10**18
hi = 0
d = 0
res = 0


for i in range(N):
    if lo > A[i]:
        lo = A[i]
        hi = 0
    if hi < A[i]:
        hi = A[i]
        if d == hi - lo:
            res += 1
        elif d < hi - lo:
            d = hi - lo
            res = 1

print(res)