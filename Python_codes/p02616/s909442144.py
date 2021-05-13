from functools import reduce

mod = 10 ** 9 + 7

N, K, *A = map(int, open(0).read().split())

A.sort(reverse=True)

ans = 1
l, r = 0, N - 1
if K % 2 == 1:
    ans = A[0]
    l = 1

if ans < 0:
    print(reduce(lambda a, b: a * b % mod, A[:K], 1))
    quit()


for i in range(K // 2):
    L = A[l] * A[l + 1]
    R = A[r] * A[r - 1]
    if L >= R:
        ans *= L
        l += 2
    else:
        ans *= R
        r -= 2
    ans %= mod

print(ans)